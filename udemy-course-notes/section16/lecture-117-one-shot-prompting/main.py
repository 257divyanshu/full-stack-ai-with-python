from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

# Use OpenAI SDK to make calls to Gemini
client = OpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

# - zero shot prompting
SYSTEM_PROMPT = "Your name is Codi. You are a coding expert. You are supposed to answer only and only coding related questions."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        # {"role": "user", "content": "Hello there Code! Write a python function that greets 'Hare Krishna Prabhuji.'."}
        {"role": "user", "content": "Hello there Code! Tell me a joke."}
    ]
)

print(response.choices[0].message.content)