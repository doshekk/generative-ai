from openai import OpenAI
import os
from dotenv import load_dotenv

os.environ.pop("OPENAI_API_KEY", None)

# Завантаження .env
load_dotenv(dotenv_path="/media/doshek/Новый том/KI-25/Основи ген. інтел/generative-ai/pract_1/.env")
api_key = os.getenv("MY_OPENAI_API_KEY")

print("🔑 API Key:", api_key)

client = OpenAI(api_key=api_key)
try:
    models = client.models.list()
    for name in models.data:
        print(name.id)
    

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Hello!"},
        ],
    )
except Exception as e:
    print("error:", e)

