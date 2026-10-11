import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY missing in .env file")

client = genai.Client(api_key=api_key)


def generate_fitness_plan(name, age, gender, goal, level, diet):
    prompt = f"""
Create a personalized general fitness plan.

Name: {name}
Age: {age}
Gender: {gender}
Goal: {goal}
Experience level: {level}
Diet preference: {diet}

Include:
1. Suitable exercises
2. Weekly workout schedule
3. Balanced food suggestions
4. Rest and recovery advice

Use simple English. Avoid extreme diets.
Mention that this is general guidance, not medical advice.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text or "Unable to generate a plan right now."