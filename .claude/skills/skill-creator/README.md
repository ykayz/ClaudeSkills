# Skill Creator

A comprehensive guide and toolkit for creating effective skills that extend Claude's capabilities.

## Overview

This skill provides everything needed to create, validate, and package new skills for Claude. It includes detailed guidance on skill design principles, creation workflows, and automated tools for skill development.

## Features

- **Skill Creation Guidance**: Step-by-step process for designing effective skills
- **Automated Initialization**: Template generation for new skills
- **Validation Tools**: Automated checking of skill structure and content
- **Packaging System**: Creates distributable skill packages

## Quick Start

### Creating a New Skill

1. **Initialize a new skill**:
   ```bash
   scripts/init_skill.py my-new-skill --path ./skills
   ```

2. **Customize the generated files**:
   - Edit `SKILL.md` with your skill's specific instructions
   - Add scripts, references, or assets as needed
   - Remove any template directories you don't need

3. **Validate your skill**:
   ```bash
   scripts/quick_validate.py ./skills/my-new-skill
   ```

4. **Package for distribution**:
   ```bash
   scripts/package_skill.py ./skills/my-new-skill
   ```

### Skill Structure

Every skill follows this structure:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter with name and description
│   └── Markdown instructions
├── scripts/ (optional)
│   └── Executable code (Python, Bash, etc.)
├── references/ (optional)
│   └── Documentation and guides
└── assets/ (optional)
    └── Templates, images, fonts, etc.
```

## Skill Creation Process

### Step 1: Understand the Use Case

Start by understanding concrete examples of how the skill will be used:

- What functionality should the skill support?
- What would users say to trigger this skill?
- What are the common workflows or tasks?

### Step 2: Plan Reusable Contents

Analyze each use case to identify reusable resources:

- **Scripts**: Code that gets rewritten repeatedly
- **References**: Documentation Claude should reference
- **Assets**: Files used in output (templates, images, etc.)

### Step 3: Initialize the Skill

Use the initialization script to create the skill structure:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

This creates:
- Skill directory with proper naming
- Template SKILL.md with TODO placeholders
- Example resource directories
- Sample files demonstrating best practices

### Step 4: Customize the Skill

Edit the generated files:

1. **SKILL.md**: Write instructions in imperative form
2. **Scripts**: Add executable code for automation
3. **References**: Include documentation and guides
4. **Assets**: Add templates and output resources

### Step 5: Validate and Package

Use the validation and packaging tools:

```bash
# Validate the skill
scripts/quick_validate.py <skill-path>

# Package for distribution
scripts/package_skill.py <skill-path> [output-directory]
```

## Best Practices

### Writing Effective SKILL.md

- Use **imperative/infinitive form** (verb-first instructions)
- Be specific about when to use the skill
- Include concrete examples
- Reference bundled resources clearly
- Keep it focused and actionable

### Skill Design Principles

1. **Progressive Disclosure**: Three-level loading system
   - Metadata (always in context)
   - SKILL.md body (when skill triggers)
   - Bundled resources (as needed)

2. **Modularity**: Each skill should be self-contained
3. **Reusability**: Include resources that prevent repeated work
4. **Clarity**: Clear naming and descriptions

### Resource Organization

- **Scripts**: For automation and deterministic tasks
- **References**: For documentation Claude should read
- **Assets**: For files used in output (not loaded into context)

## Examples

### Workflow-Based Skills
Structure for sequential processes:
```markdown
## Overview
## Workflow Decision Tree
## Step 1: [Action]
## Step 2: [Action]
```

### Task-Based Skills
Structure for tool collections:
```markdown
## Overview
## Quick Start
## [Task Category 1]
## [Task Category 2]
```

### Reference Skills
Structure for guidelines:
```markdown
## Overview
## Guidelines
## Specifications
## Usage
```

## Validation

The validation script checks:
- YAML frontmatter format
- Required fields (name, description)
- Skill naming conventions
- Directory structure
- Resource organization

## Packaging

The packaging script:
1. Validates the skill automatically
2. Creates a zip file for distribution
3. Maintains proper directory structure
4. Names the package after the skill

## Troubleshooting

### Common Issues

1. **Validation fails**: Check YAML frontmatter format
2. **Skill not triggering**: Verify name and description specificity
3. **Resources not found**: Ensure proper directory structure

### Getting Help

Use the skill's built-in help:
```bash
# General help
python claude.py skill-creator --help

# Specific guidance
python claude.py skill-creator "How do I create a PDF editing skill?"
```

## License

See LICENSE.txt for complete terms.