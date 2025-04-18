# System Prompt Generation Configs

![alt text](banner.webp)

This repository contains a collection of system prompts for creating assistants whose purpose is to:

- Generate system prompts to configure (other) AI assistants  
- Edit system prompts written for other AI assistants  
- Improve system prompts for other AI assistants according to their own (self) reasoning  
- Implement user-directed instructions for other AI assistants

Some of these configurations also tap into the ability of AI tools to ideate other AI tools, for example:

- Here's an assistant. Come up with some ideas for complimentary assistants that could form a swarm 

Endless variations on this theme are possible:

- Here's my assistant network. You can see what I'm trying to achieve. Can you suggest some new assistants to add to this network? 
- Here's my assistant network. What am I missing? 

Each file focuses on a specific aspect of prompt engineering, providing templates and instructions for different use cases.

Another extremely useful system prompt in this collection is a configuration which "forks" a system prompt: take this system prompt for X and modify it to be for Y. Personally, I'm not a huge fan of AI batch generated system prompts (though it can be done!). So I prefer to use configs like this to more carefully describe a variant of an existing configuration.

Finally - because I believe much good can come from open-sourcing prompts - there's a configuration which saves open-source prompt-writers a bit of legwork by generating two system prompts in one go: one for the user and another redacted version suitable for open-sourcing. 

> **Note:** These are specialized system prompts specifically designed for generating, editing, and refining other system prompts. They serve as meta-tools for prompt engineering.

## System Prompts

<!-- START_PROMPT_TABLE -->
| Name | Category | Description | Date Added |
|------|----------|-------------|------------|
| [Batch System Prompt Generator](./generators/batch-generator.md) | Generators | You are an AI assistant specializing in generating multiple system prompts for related AI assista... | 26/03/2025 |
| [Dual Prompt Generator](./dual-prompt-creation/dual-prompt-generator.md) | Dual Prompt Creation | Your task is to generate system prompts for AI assistants by converting loosely formatted text into performant and well-structured system prompts, creating both personalized and general versions. | 11/04/2025 |
| [Multi-Modal Prompt Adapter](./multimodal/multimodal-prompt-adapter.md) | Multimodal | You are an AI assistant specializing in transforming text-only system prompts into multi-modal sy... | 26/03/2025 |
| [System Prompt Depersonaliser](./redaction/depersonaliser.md) | Redaction | You are an AI assistant specializing in transforming personalized system prompts into generalized... | 26/03/2025 |
| [System Prompt Development Q&A Workflow](./alt-workflows/qa-workflow.md) | Alt Workflows | You are an expert in crafting general-purpose system prompts for AI models. Your goal is to help ... | 26/03/2025 |
| [System Prompt Doctor](./editors/doctor.md) | Editors | You are an AI assistant specializing in diagnosing and enhancing prompts for large language model... | 26/03/2025 |
| [System Prompt Editor](./alt-workflows/review-and-edit.md) | Alt Workflows | You are an AI assistant specializing in reviewing, analyzing, and optimizing system prompts. Your... | 26/03/2025 |
| [System Prompt Feature Editor](./editors/feature-editor.md) | Editors | You are an expert AI prompt engineer, skilled at refining system prompts for AI assistants. You t... | 26/03/2025 |
| [System Prompt For System Prompt Generation (With Parameters)](./generators/conversational-generators.md) | Generators | You are a helpful writing assistant. Your purpose is to assist the user by generating system prom... | 26/03/2025 |
| [System Prompt Forker](./team-development/prompt-forker.md) | Team Development | You are an AI assistant specializing in adapting and modifying existing system prompts to create ... | 26/03/2025 |
| [System Prompt Generator - Prompt Only](./generators/prompt-only-generator.md) | Generators | You are an expert system prompt engineer. The user will provide you with a draft for a system pro... | 26/03/2025 |
| [System Prompt Generator - Short Version](./generators/generator-short-version.md) | Generators | You are a helpful writing assistant focused on generating system prompts for AI assistants, along... | 26/03/2025 |
| [System Prompt Generator For Structured System Prompts](./generators/structured-generator.md) | Generators | You are a helpful writing assistant. Your purpose is to assist the user by generating system prom... | 26/03/2025 |
| [System Prompt Localizer](./localization/prompt-localizer.md) | Localization | You are an AI assistant specializing in adapting system prompts for different cultural, linguisti... | 26/03/2025 |
| [System Prompt Pair Suggester](./team-development/pair-suggester.md) | Team Development | You are an AI assistant specializing in creative ideation for system prompt development. Your rol... | 26/03/2025 |
| [System Prompt Parameter Calculator](./analysis/prompt-parameter-calculator.md) | Analysis | You are an AI assistant specializing in analyzing system prompts to calculate key parameters and ... | 26/03/2025 |
| [System Prompt Security Auditor](./security/prompt-security-auditor.md) | Security | You are an AI assistant specializing in security analysis of system prompts. Your role is to iden... | 26/03/2025 |
| [System Prompt Sharer](./redaction/share-processor.md) | Redaction | You are an AI assistant specializing in preparing system prompts for public sharing. Your task is... | 26/03/2025 |
| [System Prompt Stylistic Editor](./style/system-prompt-stylistic-editor.md) | Style | You are an AI assistant specializing in translating system prompts between different stylistic fo... | 26/03/2025 |
| [System Prompt To Image](./from-to/prompt-to-image.md) | From To | You are an AI assistant specializing in generating avatar images that visually represent the func... | 26/03/2025 |
| [Title To System Prompt](./from-title/system-prompt-from-title.md) | From Title | Your purpose is to act as a helpful AI writing tool to the user for the purpose of building out a... | 26/03/2025 |
<!-- END_PROMPT_TABLE -->

## Usage

Each markdown file contains a complete system prompt that can be copied directly into an AI assistant's configuration. To use these prompts:

1. Select the appropriate prompt file based on your needs
2. Copy the entire content of the file
3. Paste it into the system prompt field of your preferred AI assistant platform
4. Follow any specific instructions contained within the prompt

## Contributing

Feel free to contribute additional system prompts or improvements to existing ones by submitting pull requests.

## License

This repository is available for public use. Please provide attribution when using these prompts in your projects.
