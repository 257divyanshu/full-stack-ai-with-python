from dotenv import load_dotenv
from openai import OpenAI
import os

import json

load_dotenv()

# Use OpenAI SDK to make calls to Gemini
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format:
{ "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

Example:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }
PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }
PLAN: { "step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }
PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
PLAN: { "step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5" }
PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
PLAN: { "step": "PLAN", "content": "Now finally lets perform the add 3.5" }
PLAN: { "step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as ans" }
OUTPUT: { "step": "OUTPUT", "content": "3.5" }
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write a code to add n numbers in JS."},
        # manually keep adding messages to the History
        {"role": "assistant", "content": json.dumps({
            "step": "PLAN",
            "content": "The user wants a JavaScript function to add 'n' numbers. I should define a function that can accept a variable number of arguments."
        })},
        {"role": "assistant", "content": json.dumps({
            "step": "PLAN",
            "content": "I can use a rest parameter (...numbers) to collect all arguments passed to the function into an array. Then, I will iterate over this array and sum its elements."
        })},
        {"role": "assistant", "content": json.dumps({
            "step": "PLAN", "content": "I will initialize a sum variable to 0. Then, I will loop through the 'numbers' array using forEach or reduce and add each number to the sum."
        })},
        {"role": "assistant", "content": json.dumps({
            "step": "PLAN", "content": "Finally, I will return the calculated sum. I should also consider providing an example usage of the function."
        })},
    ]
)

print(response.choices[0].message.content)
