# Webpage to Markdown Converter

A Claude Skill that converts web pages to clean Markdown format, optimized for LLM processing and content extraction.

## Features

- **Content Extraction**: Uses readability algorithms to extract main content from web pages
- **Clean Conversion**: Converts HTML to well-formatted Markdown
- **Structure Preservation**: Maintains headings, paragraphs, links, images, and code blocks
- **Metadata Extraction**: Captures page metadata (title, author, publish date, etc.)
- **LLM-Optimized**: Output formatted for optimal LLM processing

## Why Convert Webpages to Markdown?

### 1️⃣ Remove HTML Clutter
**HTML contains complex structures**: divs, spans, classes, inline styles  
**Markdown provides clean content**: Focus on semantic meaning, not presentation  
**LLMs can process content directly**: No need to parse through HTML noise

### 2️⃣ Standardized Format
**Consistent structure**: Headings, paragraphs, lists in predictable format  
**Easy to parse**: Simple syntax that LLMs understand natively  
**Portable content**: Works across different platforms and tools

### 3️⃣ Token Efficiency
**HTML is verbose**: `<div class="article"><h1>Title</h1><p>Content</p></div>`  
**Markdown is concise**: `# Title\n\nContent`  
**Significant token savings**: Especially important for long articles

## Usage Example

**Input**: A web article URL  
**Output**: Clean Markdown with extracted content and metadata

```markdown
# Article Title

**Author**: John Doe  
**Published**: 2024-01-15  
**URL**: https://example.com/article

## Introduction

This is the main content extracted from the webpage...

## Key Points

- Point 1
- Point 2
- Point 3

## Conclusion

Final thoughts and summary...
```

## Integration with Other Skills

This skill works perfectly with:
- **md-to-json-parser**: Convert the Markdown output to structured JSON
- **Content analysis skills**: Process the clean text for summarization, classification, etc.
- **Documentation generators**: Use extracted content for documentation workflows

## Technical Details

- Uses advanced readability algorithms to identify main content
- Handles JavaScript-rendered pages when needed
- Preserves semantic HTML elements (headings, lists, code blocks)
- Extracts and includes relevant metadata
- Optimizes output for LLM consumption