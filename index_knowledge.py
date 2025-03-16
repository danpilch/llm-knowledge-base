from pathlib import Path

from agno.knowledge.docx import DocxKnowledgeBase
from agno.knowledge.text import TextKnowledgeBase
from agno.knowledge.combined import CombinedKnowledgeBase
from agno.vectordb.pgvector import PgVector
import argparse


db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
docx_path = "documents/docx/"
text_path = "documents/text/"

parser = argparse.ArgumentParser(
                    prog='knowledgebase',
                    description='Inserts documents into pgvector postgres datastore',
                    epilog='')

group = parser.add_mutually_exclusive_group()
group.add_argument("--create", action="store_true", help="Create or recreate the datastore from scratch")
group.add_argument("--upsert", action="store_true", help="Update or insert records without recreating the datastore")

args = parser.parse_args()

# Create a knowledge base with the DOCX files from the data/docs directory
docx_knowledge_base = DocxKnowledgeBase(
    path=Path(docx_path),
    vector_db=PgVector(
        table_name="docx_documents",
        db_url=db_url,
    ),
)

text_knowledge_base = TextKnowledgeBase(
    path=Path(text_path),
    vector_db=PgVector(
        table_name="text_documents",
        db_url=db_url,
    ),
    formats=[".txt", ".md"]
)

knowledge_base = CombinedKnowledgeBase(
    sources=[
		docx_knowledge_base,
		text_knowledge_base,
    ],
    vector_db=PgVector(
        # Table name: ai.combined_documents
        table_name="combined_documents",
        db_url=db_url,
    ),
    num_documents=20,
)

if args.create:
    knowledge_base.load(recreate=True, upsert=False)
if args.upsert:
    knowledge_base.load(recreate=False, upsert=True)
