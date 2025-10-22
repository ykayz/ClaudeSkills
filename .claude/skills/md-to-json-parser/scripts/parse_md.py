import markdown
from bs4 import BeautifulSoup

def parse_md(md_file_path):
    with open(md_file_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    soup = BeautifulSoup(html, "html.parser")

    result = {"title": "", "sections": []}
    current_section = {}

    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "table", "pre", "ul", "ol"]):
        if tag.name == "h1":
            result["title"] = tag.text.strip()
        elif tag.name in ["h2", "h3", "h4", "h5", "h6"]:
            if current_section:
                result["sections"].append(current_section)
            level = int(tag.name[1])
            current_section = {"heading": tag.text.strip(), "level": level, "content": []}
        elif tag.name == "p":
            if current_section:
                current_section.setdefault("content", []).append({"type": "paragraph", "text": tag.text.strip()})
        elif tag.name == "table":
            if current_section:
                headers = [th.text.strip() for th in tag.find_all("th")]
                rows = []
                tr_list = tag.find_all("tr")

                # 处理有表头的情况
                if headers:
                    for tr in tr_list[1:]:
                        cells = [td.text.strip() for td in tr.find_all("td")]
                        if cells:
                            rows.append(dict(zip(headers, cells)))
                # 处理无表头的情况
                else:
                    for tr in tr_list:
                        cells = [td.text.strip() for td in tr.find_all("td")]
                        if cells:
                            rows.append({"cells": cells})

                if rows:
                    current_section.setdefault("content", []).append({"type": "table", "rows": rows})
        elif tag.name == "pre":
            # 只处理 pre 标签，避免重复处理 pre > code
            code_tag = tag.find("code")
            if code_tag:
                code_text = code_tag.text.strip()
            else:
                code_text = tag.text.strip()

            if current_section and code_text:
                current_section.setdefault("content", []).append({"type": "code", "text": code_text})
        elif tag.name == "ul":
            if current_section:
                items = [li.text.strip() for li in tag.find_all("li", recursive=False)]
                if items:
                    current_section.setdefault("content", []).append({"type": "unordered_list", "items": items})
        elif tag.name == "ol":
            if current_section:
                items = [li.text.strip() for li in tag.find_all("li", recursive=False)]
                if items:
                    current_section.setdefault("content", []).append({"type": "ordered_list", "items": items})

    if current_section:
        result["sections"].append(current_section)

    return result
