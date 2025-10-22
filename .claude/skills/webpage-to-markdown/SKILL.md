name: webpage-to-markdown
description: Convert web pages to clean Markdown format, extracting main content while preserving structure. This skill should be used when users need to convert web pages to markdown, extract content from websites, save web articles as markdown, convert HTML to markdown, archive web content, or process online documentation. Keywords: 网页转markdown, 网页转换, HTML转markdown, 提取网页内容, 保存网页为markdown, convert webpage to markdown, extract web content, save article as markdown, HTML to markdown conversion, web scraping to markdown, 网页内容提取, 在线文档转换
inputs:
  - url
  - options (optional)
outputs:
  - markdown_content
  - metadata
instructions: |
  # Webpage to Markdown Converter
  
  This skill fetches web pages and converts them to clean, readable Markdown format. It uses readability algorithms to extract the main content while preserving the document structure and formatting.
  
  ## When to Use This Skill
  
  Use this skill when you need to:
  - Convert web articles or documentation to Markdown
  - Extract readable content from web pages
  - Process web content for analysis or transformation
  - Archive web content in a readable format
  - Prepare web content for further processing
  
  ## Processing Steps
  
  ### Step 1: Fetch Web Page Content
  - Validate the provided URL format
  - Send HTTP GET request with appropriate headers
  - Handle redirects and follow them safely
  - Manage different character encodings
  - Handle network errors and timeouts gracefully
  
  ### Step 2: Parse HTML Structure
  - Parse HTML using a robust parser
  - Identify the main content area using readability heuristics
  - Remove navigation, ads, sidebars, and other non-content elements
  - Preserve the document's logical structure
  - Handle malformed HTML gracefully
  
  ### Step 3: Extract Main Content
  - Use readability algorithms to identify primary content
  - Preserve headings and their hierarchy (H1-H6)
  - Maintain paragraph structure and flow
  - Keep important formatting elements
  - Extract images with their alt text and sources
  - Preserve links with proper anchor text
  
  ### Step 4: Convert to Markdown
  - Convert headings to appropriate Markdown levels
  - Transform paragraphs to Markdown format
  - Convert lists (ordered and unordered) to Markdown syntax
  - Handle code blocks with language detection
  - Convert tables to Markdown table format
  - Preserve emphasis (bold, italic) formatting
  - Handle blockquotes appropriately
  
  ### Step 5: Generate Clean Output
  - Remove excessive whitespace and blank lines
  - Ensure consistent formatting throughout
  - Validate Markdown syntax
  - Optimize for readability
  - Preserve important semantic information
  
  ## Optional Parameters
  
  The options parameter can include:
  - `include_images`: Whether to include images (default: true)
  - `preserve_links`: Whether to keep all links (default: true)
  - `extract_metadata`: Whether to extract page metadata (default: true)
  - `content_selector`: CSS selector for specific content extraction
  - `exclude_selectors`: CSS selectors for elements to exclude
  
  ## Output Format
  
  Returns an object containing:
  ```json
  {
    "markdown_content": "# Article Title\n\nArticle content in Markdown format...",
    "metadata": {
      "title": "Original Page Title",
      "author": "Article Author",
      "publish_date": "2024-01-15",
      "url": "https://example.com/article",
      "word_count": 1250,
      "reading_time": 5,
      "extraction_success": true
    }
  }
  ```
  
  ## Content Preservation
  
  The converter preserves:
  - **Headings**: Maintains heading hierarchy (H1 → #, H2 → ##, etc.)
  - **Paragraphs**: Clean paragraph breaks and spacing
  - **Lists**: Both ordered (1., 2., 3.) and unordered (-, *, +) lists
  - **Code Blocks**: With language detection and proper fencing
  - **Links**: Internal and external links with descriptive text
  - **Images**: With alt text and source URLs
  - **Tables**: Converted to Markdown table syntax
  - **Emphasis**: Bold (**text**) and italic (*text*) formatting
  - **Blockquotes**: Preserved with > syntax
  
  ## Error Handling
  
  - Invalid URLs: Return appropriate error messages
  - Network failures: Handle timeouts and connection issues
  - Malformed HTML: Gracefully handle poorly formatted pages
  - Missing content: Return meaningful error if no content found
  - Encoding issues: Handle various character encodings
  - Large pages: Manage memory efficiently for large documents