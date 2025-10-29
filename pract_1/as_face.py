from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

env_loaded = load_dotenv(dotenv_path="e:/Основи ген. інтел/generative-ai/pract_1/.env")
print("Файл .env завантажено", env_loaded)

api_token = os.getenv("HUGGING_FACE_API_KEY")
print("Значення токена", api_token)

api = HfApi()

try:
    user_info = api.whoami(token=api_token)
    print("API-ключ дійсний.", user_info['name'])
except Exception as e:
    print("Помилка:", e)