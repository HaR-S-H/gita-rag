from fastapi import APIRouter
from app.retrieval import query_verse
from app.generator import generate_response

router = APIRouter()

@router.get("/query")
def get_answer(query: str):
    relevant_verses = query_verse(query)
    context = "\n".join([v["verse_text"] for v in relevant_verses])
    response = generate_response(context, query)
    return {"response": response, "verses": relevant_verses}
