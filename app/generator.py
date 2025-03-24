import google.generativeai as genai
from app.config import GOOGLE_API_KEY

# Configure Gemini 2.0 Flash
genai.configure(api_key=GOOGLE_API_KEY)
llm_model = genai.GenerativeModel("gemini-2.0-flash")  # Updated model

def generate_response(context, query):
    user_message = f"""
    Context:
    {context}
    ---------------------
    Answer the query strictly based on context: {query}
    """
    chat = llm_model.start_chat(history=[{"role": "user", "parts": [user_message]}])
    return chat.send_message(user_message).text
