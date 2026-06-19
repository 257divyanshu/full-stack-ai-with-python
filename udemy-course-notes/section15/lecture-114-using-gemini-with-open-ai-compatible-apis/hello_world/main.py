from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

# Use OpenAI SDK to make calls to Gemini
client = OpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Who are you? And who built you?"}
    ]
)

print(response.choices[0].message.content)