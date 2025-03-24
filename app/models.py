from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5

class SimilarVerse(BaseModel):
    verse_text: str
    similarity_score: float

class QueryResponse(BaseModel):
    results: List[SimilarVerse]

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str
