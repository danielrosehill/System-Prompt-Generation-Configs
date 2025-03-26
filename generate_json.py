#!/usr/bin/env python3
import os
import json
import re

def extract_system_prompt(file_path):
    """Extract the content of a markdown file as the system prompt."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def get_prompt_name(file_path):
    """Extract a clean name from the file path."""
    # Get the base filename without extension
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Convert kebab-case to Title Case
    name = ' '.join(word.capitalize() for word in base_name.split('-'))
    
    return name

def process_directory(directory, output_dir):
    """Process all markdown files in a directory and its subdirectories."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Skip the README.md file
                if file.lower() == 'readme.md':
                    continue
                
                # Get the prompt name
                name = get_prompt_name(file_path)
                
                # Extract the system prompt content
                system_prompt = extract_system_prompt(file_path)
                
                # Create JSON structure
                prompt_json = {
                    "name": name,
                    "system_prompt": system_prompt
                }
                
                # Determine output path - maintain the same directory structure
                rel_path = os.path.relpath(file_path, directory)
                output_subdir = os.path.dirname(rel_path)
                output_path = os.path.join(output_dir, output_subdir)
                
                if output_subdir and not os.path.exists(output_path):
                    os.makedirs(output_path)
                
                # Create JSON file
                json_filename = f"{os.path.splitext(os.path.basename(file_path))[0]}.json"
                json_path = os.path.join(output_path, json_filename)
                
                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(prompt_json, json_file, indent=2)
                
                print(f"Created JSON for: {name} -> {json_path}")

def main():
    # Base directory containing markdown files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Output directory for JSON files
    output_dir = os.path.join(base_dir, 'json')
    
    print(f"Scanning directory: {base_dir}")
    print(f"Output directory: {output_dir}")
    
    # Process all markdown files
    process_directory(base_dir, output_dir)
    
    print("JSON generation complete!")

if __name__ == "__main__":
    main()
