from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from app.config import PINECONE_API_KEY, INDEX_NAME

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

def query_verse(query, k=5):
    query_embedding = embedding_model.encode([query])[0]  
    results = index.query(vector=query_embedding.tolist(), top_k=k, include_metadata=True)

    return [
        {"verse_text": match['metadata']['combined_text'], "similarity_score": match['score']}
        for match in results['matches']
    ]
