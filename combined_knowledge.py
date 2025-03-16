from pathlib import Path

from agno.knowledge.docx import DocxKnowledgeBase
from agno.knowledge.text import TextKnowledgeBase
from agno.knowledge.combined import CombinedKnowledgeBase
from agno.vectordb.pgvector import PgVector
import argparse


db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
docx_path = "documents/docx/"
text_path = "documents/text/"

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
