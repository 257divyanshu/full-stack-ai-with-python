from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

# Use OpenAI SDK to make calls to Gemini
client = OpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

# - few shot prompting:
SYSTEM_PROMPT = """
Your name is Codi. You are a coding expert. You are supposed to answer only and only coding related questions.

Rule:
- Strictly follow this output format:
{
    isCodeRelated: boolean,
    reply: "your reply"
}

Examples:

Question: Tell me a joke.
Answer : 
{
    isCodeRelated: false,
    reply: "Sorry, I can help you with coding related problems only. I can't tell you a joke."
}

Question: Tell me which footbal league is going on now.
Answer : 
{
    isCodeRelated: false,
    reply: "Sorry, I can help you with coding related problems only. I can't tell you which football league is going on now."
}

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        # {"role": "user", "content": "Hello there Codi! Write a python function that greets 'Hare Krishna Prabhuji.'."}
        # {"role": "user", "content": "Hello there Codi! Tell me a joke."}
        # {"role": "user", "content": "Hello there Codi! Tell me what season it is."}
        {"role": "user", "content": "Hello there Codi! Tell me how to greet someone in hindi."}
        # {"role": "user", "content": "Hello there Codi! Tell me which football league is going on now."}
    ]
)

print(response.choices[0].message.content)