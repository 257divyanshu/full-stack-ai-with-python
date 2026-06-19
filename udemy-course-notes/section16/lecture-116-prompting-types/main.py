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
        {"role": "system", "content": "You are an expert in Mathematics and you are supposed to answer only and only math related questions."},
        # {"role": "user", "content": "Who are you? And who built you?"}
        # {"role": "user", "content": "Hello there! What's up Gemini?"}
        # {"role": "user", "content": "Hello there Gemini! Tell me how to greet someone in Hindi"}
        {"role": "user", "content": "Hello there Gemini! Briefly state the Pythagoras theorem with its formula."}
    ]
)

print(response.choices[0].message.content)