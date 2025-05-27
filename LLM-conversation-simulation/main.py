from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)

response = client.responses.create(
    model="o4-mini",
    input="""
            Generate 30 short dialogues between Leon S. Kennedy (determined, a bit earnest) and Ada Wong (enigmatic, resourceful). Each dialogue should be a brief exchange between them, reflecting their distinct personalities and their typical interactions—often involving cryptic information, emotional tension, or a shared objective approached from different angles.

            Each dialogue should be returned in JSON format, where each object has the keys:

            "Leon S. Kennedy": Leon’s line

            "Ada Wong": Ada’s line

            """
)

print(response.output_text)