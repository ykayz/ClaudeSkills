# Shared Claude Skills

A modular Claude Skill collection designed for task automation, document parsing, and intelligent dispatch. Includes utilities for webpage-to-Markdown conversion, API doc parsing, and structured JSON extraction—optimized for LLM-driven workflows.

## 🚀 Available Skills

### Document Processing

- **[md-to-json-parser](.claude/skills/md-to-json-parser/README.md)** - Convert Markdown documents to structured JSON format

  - Parse headings, paragraphs, tables, and code blocks
  - Extract structured data from markdown files
  - Support for complex document structures
- **[webpage-to-markdown](.claude/skills/webpage-to-markdown/README.md)** - Convert web pages to clean Markdown format

  - Extract main content while preserving structure
  - Handle metadata extraction and content cleaning
  - Support for various webpage formats

### Skill Development

- **[skill-creator](.claude/skills/skill-creator/README.md)** - Comprehensive toolkit for creating Claude Skills
  - Initialize new skills with proper structure
  - Validate skill configurations and content
  - Package skills for distribution
  - Follow best practices and design principles

## 🎯 Key Features

- **Modular Design**: Each skill is self-contained with clear interfaces
- **Bilingual Support**: Enhanced with Chinese and English keywords for better trigger rates
- **Progressive Disclosure**: Skills use step-by-step workflows for complex tasks
- **Error Handling**: Comprehensive error management and validation
- **Documentation**: Detailed README files with examples and best practices

## 📋 Usage

Skills are automatically available when using Claude with this repository. Simply describe your task and Claude will select the appropriate skill based on your request.

## 🛠️ Development

Skills are organized in the `.claude/skills/` directory with the following structure:

```
.claude/skills/
├── skill-name/
│   ├── SKILL.md          # Core skill definition
│   ├── README.md         # Detailed documentation
│   ├── LICENSE.txt       # License information
│   └── scripts/          # Optional scripts and utilities
```

## 📄 License

See individual skill LICENSE.txt files for specific licensing terms.
