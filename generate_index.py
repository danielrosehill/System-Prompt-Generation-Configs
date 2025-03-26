#!/usr/bin/env python3
import os
import re
from datetime import datetime
from pathlib import Path

def extract_metadata(file_path):
    """Extract metadata from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def clean_description(text):
            # Remove markdown formatting
            text = re.sub(r'#+ *', '', text)
            text = re.sub(r'\*\*|__', '', text)
            # Remove multiple spaces and newlines
            text = re.sub(r'\s+', ' ', text)
            # Remove "Purpose" if it starts with it
            text = re.sub(r'^Purpose\s*', '', text)
            # Truncate to reasonable length
            if len(text) > 100:
                text = text[:97] + '...'
            return text.strip()
            
        # Extract title from first h1 heading
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else Path(file_path).stem.replace('-', ' ').title()
        
        # Extract description from first paragraph after title
        desc_match = re.search(r'^#.*?\n\n(.+?)(?=\n\n|\Z)', content, re.DOTALL)
        description = desc_match.group(1).replace('\n', ' ').strip() if desc_match else ''
        description = clean_description(description)
        # Determine category from directory structure
        category = Path(file_path).parent.name.replace('-', ' ').title()
        
        # Get file modification date
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        date = mod_time.strftime("%d/%m/%Y")

        return {
            'name': title,
            'category': category,
            'description': description,
            'date': date,
            'path': str(file_path)
        }
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None

def generate_table(prompts):
    """Generate markdown table from prompt metadata."""
    if not prompts:
        return "No prompts found."
    
    # Sort prompts alphabetically by name
    prompts.sort(key=lambda x: x['name'].lower())
    
    # Generate table rows
    rows = []
    rows.append("| Name | Category | Description | Date Added |")
    rows.append("|------|----------|-------------|------------|")
    
    for prompt in prompts:
        name_link = f"[{prompt['name']}](./{prompt['path']})"
        row = f"| {name_link} | {prompt['category']} | {prompt['description']} | {prompt['date']} |"
        rows.append(row)
    
    return '\n'.join(rows)

def update_readme(table_content):
    """Update README.md with generated table."""
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace content between markers
        pattern = r'(<!-- START_PROMPT_TABLE -->).*(<!-- END_PROMPT_TABLE -->)'
        new_content = re.sub(
            pattern,
            f'<!-- START_PROMPT_TABLE -->\n{table_content}\n<!-- END_PROMPT_TABLE -->',
            content,
            flags=re.DOTALL
        )
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print("README.md updated successfully!")
    except Exception as e:
        print(f"Error updating README.md: {str(e)}")

def main():
    prompt_dir = 'prompt-library'
    prompt_dir_path = Path(prompt_dir)
    
    if not prompt_dir_path.is_dir():
        print(f"Looking for directory: {os.path.abspath(prompt_dir)}")
        print("Error: prompt_library directory not found!")
        return
    
    # Collect all markdown files
    prompts = []
    for file_path in prompt_dir_path.rglob('*.md'):
        print(f"Processing file: {file_path}")
        metadata = extract_metadata(file_path)
        if metadata:
            prompts.append(metadata)
    
    if not prompts:
        print("No prompt files found!")
        return
    
    # Generate and update table
    table = generate_table(prompts)
    update_readme(table)

if __name__ == '__main__':
    main()