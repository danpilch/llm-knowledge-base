# llm-knowledge-base
Agno knowledgebase concept applied to example text and docx datasets of
popular William Shakespere works.

This project intends to illustrate how level 3 LLM multimodal agents can work together to provide a rich knowledge base solution.


## Requirements
python >3.12
docker
openai or whatever LLM you decide to use API KEY (in this proof-of-concept I am using `OPENAI_API_KEY`.`
[uv](https://github.com/astral-sh/uv)

## Install (this assumes installation on osx)

```bash
# Make sure python >3.12 installed
brew install uv

# Use uv pip to or whatever your preferred python library installation method
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Start up the pgvector database
make start-pgvector

# Create pgvector table and document vectors
make generate-pgvector-dimensions
```
