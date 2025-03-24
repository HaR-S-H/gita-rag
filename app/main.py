from fastapi import FastAPI
from app.models import QueryRequest, QueryResponse, SimilarVerse, ChatRequest, ChatResponse
from app.services import query_verse, pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bhagavad Gita Assistant is running!"}

@app.post("/query", response_model=QueryResponse)
async def get_similar_verses(request: QueryRequest):
    results = query_verse(request.query, request.top_k)
    return {"results": results}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_gita(request: ChatRequest):
    response_text = pipeline(request.query)
    return {"answer": response_text}
