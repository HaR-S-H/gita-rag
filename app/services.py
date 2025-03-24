from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import google.generativeai as genai
from app.config import GOOGLE_API_KEY, PINECONE_API_KEY, PINECONE_INDEX_NAME

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Pinecone setup
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

# Google Gemini 2.0 Flash setup
genai.configure(api_key=GOOGLE_API_KEY)
llm_model = genai.GenerativeModel("gemini-2.0-flash")

def query_verse(query, k=5):
    """Retrieve the top-k most similar Bhagavad Gita verses based on semantic similarity."""
    query_embedding = embedding_model.encode([query])[0]
    results = index.query(vector=query_embedding.tolist(), top_k=k, include_metadata=True)

    return [
        {"verse_text": match['metadata']['combined_text'], "similarity_score": match['score']}
        for match in results['matches']
    ]

def pipeline(query):
    """Generate an answer based on retrieved Bhagavad Gita verses using Gemini 2.0 Flash."""
    relevant_documents = query_verse(query)
    context = "\n".join([doc['verse_text'] for doc in relevant_documents])

    system_message = """
    You are an expert in the Bhagavad Gita.
    You ONLY answer questions related to the Bhagavad Gita.
    If the question is unrelated, respond with: "I don't know. Not enough information received."
    """

    user_message = f"""
    Context:
    {context}
    ---------------------
    Answer the question: {query}
    ---------------------
    """

    response = llm_model.generate_content([system_message, user_message])
    return response.text
