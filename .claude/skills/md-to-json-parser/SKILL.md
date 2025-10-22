name: md-to-json-parser
description: Structure Markdown documents into JSON, supporting headings, paragraphs, tables, code blocks, etc. This skill should be used when users need to parse markdown files, convert markdown to structured data, extract content from markdown documents, analyze markdown structure, or process .md files programmatically. Keywords: markdown解析, markdown转JSON, 提取markdown结构, 分析markdown文档, parse markdown, convert md to json, extract markdown content, markdown structure analysis, process markdown files, 处理markdown文件
inputs:
  - md_file_path
outputs:
  - structured_json
instructions: |
  # Markdown to JSON Parser
  
  This skill parses Markdown documents and converts them into structured JSON format, making it easier for Claude to understand and work with document content programmatically.
  
  ## When to Use This Skill
  
  Use this skill when you need to:
  - Extract structured data from Markdown files
  - Convert documentation into JSON for processing
  - Analyze document structure and content
  - Process Markdown files programmatically
  
  ## Processing Steps
  
  ### Step 1: Load and Validate Markdown File
  - Read the Markdown file from the provided path
  - Validate file exists and is readable
  - Handle encoding issues (default to UTF-8)
  
  ### Step 2: Parse Document Structure
  - Extract headings (H1-H6) with their hierarchy
  - Identify paragraphs and text content
  - Locate tables and convert to structured format
  - Find code blocks with their language annotations
  - Detect lists (ordered and unordered)
  - Identify links, images, and other inline elements
  
  ### Step 3: Convert Tables to Arrays
  - Parse table headers as column names
  - Convert each row to a JSON object
  - Preserve cell content with proper escaping
  - Handle merged cells appropriately
  
  ### Step 4: Preserve Code Blocks
  - Maintain original formatting and indentation
  - Preserve language annotations
  - Keep special characters and syntax intact
  - Handle multi-line code blocks correctly
  
  ### Step 5: Generate Structured JSON Output
  - Create hierarchical structure reflecting document organization
  - Include metadata like word count, heading count, etc.
  - Preserve relationships between elements
  - Ensure JSON is valid and well-formed
  
  ## Output Format
  
  The structured JSON includes:
  ```json
  {
    "metadata": {
      "title": "Document Title",
      "word_count": 1500,
      "heading_count": 8,
      "table_count": 3,
      "code_block_count": 5
    },
    "structure": {
      "headings": [
        {"level": 1, "text": "Main Title", "id": "main-title"}
      ],
      "paragraphs": [
        {"text": "Content...", "word_count": 120}
      ],
      "tables": [
        {
          "headers": ["Column1", "Column2"],
          "rows": [
            {"Column1": "data1", "Column2": "data2"}
          ]
        }
      ],
      "code_blocks": [
        {
          "language": "python",
          "content": "def example():\n    pass"
        }
      ]
    }
  }
  ```
  
  ## Error Handling
  
  - Handle missing files gracefully
  - Manage encoding issues
  - Deal with malformed Markdown
  - Report parsing errors clearly
  - Validate JSON output format
