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

# Check the Makefile help for all available commands
make help
agno-knowledge-base:a4b92f4
create-pgvector-dimensions:Update pgvector table and document vectors for an existing table
create-pgvector:Create the pgvector datastore docker container
destroy-pgvector:Destroy the pgvector datastore docker container
help:          Show this help message
run:           Run the application
start-pgvector:Start an existing pgvector datastore docker container
upsert-pgvector-dimensions:Update pgvector table and document vectors for an existing table

# Start up the pgvector database
make start-pgvector

# Create pgvector table and document vectors
make create-pgvector-dimensions

# Start the application
make run

# You'll see something like:
make run
python agent.py
INFO     Embedder not provided, using OpenAIEmbedder as default.
INFO     Embedder not provided, using OpenAIEmbedder as default.
INFO     Embedder not provided, using OpenAIEmbedder as default.
INFO     Starting playground on http://localhost:7777
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Agent Playground ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                             ┃
┃                                                                             ┃
┃  Playground URL: https://app.agno.com/playground?endpoint=localhost%3A7777  ┃
┃                                                                             ┃
┃                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
INFO:     Will watch for changes in these directories: ['/Users/dpilch/Documents/playground/llm-knowledge-base']
INFO:     Uvicorn running on http://localhost:7777 (Press CTRL+C to quit)
INFO:     Started reloader process [50014] using StatReload
INFO     Embedder not provided, using OpenAIEmbedder as default.
INFO     Embedder not provided, using OpenAIEmbedder as default.
INFO     Embedder not provided, using OpenAIEmbedder as default.
INFO:     Started server process [50027]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
