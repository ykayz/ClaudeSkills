## Why JSON is More Efficient Than Markdown

### 1️⃣ Clear Structure, Reduced Redundancy

**Markdown is designed for human reading**, containing numerous formatting symbols (like `#`, `*`, `|`, space indentation)
**JSON is machine-friendly**, directly expressing structural relationships without format interpretation
**LLMs processing JSON can skip format parsing and go straight to semantic understanding**

✅ **Example Comparison:**

**Markdown Format:**

```markdown
| Name  | Type | Description |
|-------|------|-------------|
| limit | int  | Max users   |
```

**JSON Format:**

```json
[{ "Name": "limit", "Type": "int", "Description": "Max users" }]
```

→ The latter is more compact, structurally clear, and uses fewer tokens

### 2️⃣ Easy for Search and Matching

JSON can be directly used for:

- **Key-value retrieval**
- **Embedding retrieval**
- **Vector matching**

LLMs can quickly locate fields like `parameters.limit.type` without line-by-line scanning of Markdown

### 3️⃣ Supports Multi-round Task Scheduling

In Claude Skill or RD-Agent, JSON can be passed as intermediate state:

**Step 1**: Parse Markdown → JSON
**Step 2**: Generate calling code / test samples / document summaries based on JSON
**Step 3**: When Claude answers "Does this API support pagination?", just query the JSON

### 🧠 Bonus: Actual Token Savings

| Format   | Avg Token Count         | Processing Efficiency | Suitable Task Types                |
| -------- | ----------------------- | --------------------- | ---------------------------------- |
| Markdown | High (with formatting)  | Medium                | Human reading, display             |
| JSON     | Low (compact structure) | High                  | LLM parsing, scheduling, retrieval |
| YAML     | Medium                  | High                  | Skill definition, config files     |
