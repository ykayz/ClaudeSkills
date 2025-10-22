#!/usr/bin/env python3
"""
Webpage to Markdown Converter
A Claude Skill for converting web pages to clean Markdown format
"""

import requests
import re
from urllib.parse import urljoin, urlparse
from datetime import datetime

try:
    from bs4 import BeautifulSoup
    import html2text
    DEPENDENCIES_AVAILABLE = True
except ImportError:
    DEPENDENCIES_AVAILABLE = False


class WebpageToMarkdown:
    def __init__(self, options=None):
        """Initialize with optional configuration"""
        if not DEPENDENCIES_AVAILABLE:
            raise ImportError("Required packages not installed: beautifulsoup4, html2text, requests")

        # Default options
        self.options = {
            'include_images': True,
            'preserve_links': True,
            'extract_metadata': True,
            'content_selector': None,
            'exclude_selectors': []
        }

        # Update with user options
        if options:
            self.options.update(options)

        # Configure html2text
        self.h = html2text.HTML2Text()
        self.h.ignore_links = not self.options['preserve_links']
        self.h.ignore_images = not self.options['include_images']
        self.h.body_width = 0  # No line wrapping

        self.base_url = None  # Will be set when processing URL
        
    def validate_url(self, url):
        """Validate URL format and scheme"""
        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                raise ValueError("Invalid URL format: missing scheme or domain")
            if result.scheme not in ['http', 'https']:
                raise ValueError(f"Unsupported URL scheme: {result.scheme}. Only http and https are supported")
            return True
        except Exception as e:
            raise ValueError(f"Invalid URL: {str(e)}")

    def fetch_webpage(self, url):
        """Fetch webpage content with proper headers"""
        # Validate URL first
        self.validate_url(url)
        self.base_url = url

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.Timeout:
            raise Exception("Request timeout: The webpage took too long to respond")
        except requests.ConnectionError:
            raise Exception("Connection error: Could not connect to the webpage")
        except requests.HTTPError as e:
            raise Exception(f"HTTP error {e.response.status_code}: {e.response.reason}")
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch webpage: {str(e)}")
    
    def extract_metadata(self, soup, url):
        """Extract metadata from the webpage"""
        metadata = {
            'url': url,
            'title': '',
            'author': '',
            'published_date': '',
            'description': '',
            'extracted_at': datetime.now().isoformat()
        }
        
        # Extract title
        title_tag = soup.find('title')
        if title_tag:
            metadata['title'] = title_tag.get_text().strip()
        
        # Extract meta tags
        meta_tags = {
            'author': ['author', 'article:author', 'dc.creator'],
            'description': ['description', 'og:description', 'twitter:description'],
            'published_date': ['article:published_time', 'datePublished', 'pubdate', 'date']
        }
        
        for key, names in meta_tags.items():
            for name in names:
                tag = soup.find('meta', attrs={'name': name}) or soup.find('meta', attrs={'property': name})
                if tag and tag.get('content'):
                    metadata[key] = tag['content'].strip()
                    break
        
        return metadata
    
    def extract_main_content(self, soup):
        """Extract main content using readability heuristics"""
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header", "aside"]):
            script.decompose()

        # Remove elements based on exclude_selectors
        for selector in self.options.get('exclude_selectors', []):
            for element in soup.select(selector):
                element.decompose()

        # Use custom content selector if provided
        if self.options.get('content_selector'):
            main_content = soup.select_one(self.options['content_selector'])
            if main_content:
                return main_content

        # Try to find main content areas
        content_selectors = [
            'main', 'article', '[role="main"]', '.main-content', '.content',
            '.post-content', '.entry-content', '.article-content'
        ]

        main_content = None
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break

        # Fallback to body if no main content found
        if not main_content:
            main_content = soup.find('body')

        return main_content if main_content else soup
    
    def convert_relative_urls(self, soup):
        """Convert relative URLs to absolute URLs"""
        if not self.base_url:
            return

        # Convert image src attributes
        for img in soup.find_all('img'):
            if img.get('src'):
                img['src'] = urljoin(self.base_url, img['src'])

        # Convert link href attributes
        for link in soup.find_all('a'):
            if link.get('href'):
                link['href'] = urljoin(self.base_url, link['href'])

    def convert_to_markdown(self, html_content, url):
        """Convert HTML to Markdown with metadata"""
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract metadata if enabled
        metadata = {}
        if self.options.get('extract_metadata', True):
            metadata = self.extract_metadata(soup, url)

        # Extract main content
        main_content = self.extract_main_content(soup)

        # Convert relative URLs to absolute
        self.convert_relative_urls(main_content)

        # Convert to markdown
        markdown_content = self.h.handle(str(main_content))

        # Clean up markdown
        markdown_content = self.clean_markdown(markdown_content)

        # Calculate statistics
        word_count = len(markdown_content.split())
        reading_time = max(1, word_count // 200)  # Assume 200 words per minute

        # Format with metadata
        formatted_output = self.format_output(markdown_content, metadata)

        return {
            'markdown_content': formatted_output,
            'metadata': {
                **metadata,
                'word_count': word_count,
                'reading_time': reading_time,
                'extraction_success': True
            }
        }
    
    def clean_markdown(self, markdown):
        """Clean up markdown content"""
        # Remove excessive blank lines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        # Remove leading/trailing whitespace
        markdown = markdown.strip()

        return markdown
    
    def format_output(self, markdown_content, metadata):
        """Format output with metadata header"""
        header_parts = []
        
        if metadata.get('title'):
            header_parts.append(f"# {metadata['title']}\n")
        
        metadata_lines = []
        if metadata.get('author'):
            metadata_lines.append(f"**Author**: {metadata['author']}")
        if metadata.get('published_date'):
            metadata_lines.append(f"**Published**: {metadata['published_date']}")
        if metadata.get('url'):
            metadata_lines.append(f"**URL**: {metadata['url']}")
        
        if metadata_lines:
            header_parts.append("\n".join(metadata_lines) + "\n")
        
        header = "\n".join(header_parts) + "\n---\n\n"
        
        return header + markdown_content
    
    def process_url(self, url):
        """Main method to process a URL and return markdown"""
        try:
            html_content = self.fetch_webpage(url)
            result = self.convert_to_markdown(html_content, url)
            return result
        except ValueError as e:
            return {
                'error': str(e),
                'markdown_content': '',
                'metadata': {'extraction_success': False}
            }
        except Exception as e:
            return {
                'error': str(e),
                'markdown_content': '',
                'metadata': {'extraction_success': False}
            }


# Public API function for Claude Code to use
def convert_webpage_to_markdown(url, options=None):
    """
    Convert a webpage to Markdown format.

    Args:
        url (str): The URL of the webpage to convert
        options (dict, optional): Configuration options
            - include_images (bool): Whether to include images (default: True)
            - preserve_links (bool): Whether to keep all links (default: True)
            - extract_metadata (bool): Whether to extract page metadata (default: True)
            - content_selector (str): CSS selector for specific content extraction
            - exclude_selectors (list): CSS selectors for elements to exclude

    Returns:
        dict: Result containing:
            - markdown_content (str): The converted markdown
            - metadata (dict): Extracted metadata including title, author, etc.
            - error (str, optional): Error message if conversion failed

    Example:
        >>> result = convert_webpage_to_markdown('https://qlib.readthedocs.io/en/latest/')
        >>> print(result['markdown_content'])
        >>> print(result['metadata']['title'])
    """
    if not DEPENDENCIES_AVAILABLE:
        return {
            'error': 'Required packages not installed: beautifulsoup4, html2text, requests',
            'markdown_content': '',
            'metadata': {'extraction_success': False}
        }

    converter = WebpageToMarkdown(options)
    return converter.process_url(url)
