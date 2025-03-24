from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Bhagavad Gita Assistant")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Bhagavad Gita Assistant API is running!"}
