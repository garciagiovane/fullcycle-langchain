import os
from dotenv import load_dotenv
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()
for k in ("OPENAI_API_KEY", "GOOGLE_API_KEY", "OPENROUTER_API_KEY", "OPEN_AI_MODEL", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise ValueError(f"Missing environment variable: {k}")
    
query = "Tell me more about the gpt-5 thinking, evaluation and performance results comparing to gpt-4"
embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("OPEN_AI_MODEL", "gemini-embedding-2"))
store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION", ""),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

results = store.similarity_search_with_score(query, k=10)
for i, (doc, score) in enumerate(results, start=1):
    print("=" * 50)
    print(f"Result {i} (Score: {score:.2f})")
    print("=" * 50)

    print("\nContent:\n")
    print(doc.page_content.strip())

    print("\nMetadata:\n")
    for key, value in doc.metadata.items():
        print(f"{key}: {value}")
    