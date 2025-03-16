from agno.playground import Playground, serve_playground_app
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.vectordb.pgvector import PgVector, SearchType
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.agent import Agent
from combined_knowledge import knowledge_base
import argparse
import os

parser = argparse.ArgumentParser(
                    prog='python agent.py',
                    description='Runs Agno agents to analyse and chat with the works of William Shakespere.',
                    epilog='"I am not bound to please thee with my answers." – The Merchant of Venice')

parser.add_argument("--groq", action="store_true", help="Use Groq API instead of OpenAI")
parser.add_argument("--port", type=int, default=7777, help="Port to bind agent to on localhost")
args = parser.parse_args()

db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"

# Agent config
description="You are the knowledge base of interesting facts about William Shakespere and his works"
instructions="Provide a summary of information about William Shakespeare's works, using the search_knowledge_base tool to access relevant context."

# The default agent of choice using OpenAI Chat
openai_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    description=description,
    instructions=instructions,
    storage=PostgresAgentStorage(table_name="agent_sessions_openai", db_url=db_url),
    search_knowledge=True,
    add_history_to_messages=True,
    read_chat_history=True,
    show_tool_calls=True,
    markdown=True,
)

# Groq has a generous free tier you'll need to signup and get an API key. caveat, max of 6000 token context
groq_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", max_tokens=6000),
    knowledge=knowledge_base,
    description=description,
    instructions=instructions,
    storage=PostgresAgentStorage(table_name="agent_sessions_groq", db_url=db_url),
    search_knowledge=True,
    add_history_to_messages=True,
    read_chat_history=True,
    show_tool_calls=True,
    markdown=True,
)

if args.groq:
    app = Playground(agents=[groq_agent]).get_app()
else:
    app = Playground(agents=[openai_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("agent:app", reload=True, port=args.port)
