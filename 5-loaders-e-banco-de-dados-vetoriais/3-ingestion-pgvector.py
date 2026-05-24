import os
from  pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector
from langchain_core.documents import Document

load_dotenv()
for k in ("OPENAI_API_KEY", "GOOGLE_API_KEY", "OPENROUTER_API_KEY", "OPEN_AI_MODEL", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise ValueError(f"Missing environment variable: {k}")
    
current_dir = Path(__file__).parent
pdf_path = current_dir / "gpt5.pdf"

loader = PyPDFLoader(str(pdf_path))
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=150, add_start_index=False
    )
 
chunks = splitter.split_documents(docs)

if not chunks:
    raise SystemExit(
        "No chunks were created from the document. Please check the PDF file and the splitting parameters."
        )

enriched = [
    Document(
        page_content=chunk.page_content,
        metadata={k: v for k, v in chunk.metadata.items() if v not in ("", None)},
    )
    for chunk in chunks
]

ids = [f"doc-{i}" for i in range(len(enriched))]

embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("OPEN_AI_MODEL", "gemini-embedding-2"))

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION", ""),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

store.add_documents(enriched, ids=ids)