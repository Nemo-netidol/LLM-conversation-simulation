from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
        "role": "user",
        "content": """
            Generate a continuous conversation between Leon S. Kennedy (determined, a bit earnest) and Ada Wong (enigmatic, resourceful), consisting of 30 exchanges (15 from each character).

            The dialogue should unfold like a coherent scene, where each exchange builds upon the previous one — not isolated topics. Their interaction should reflect their distinct personalities, with emotional tension, cryptic information, and differing approaches to a shared objective.

            Return the conversation in JSON format only, where each exchange is an object with:

                "Leon S. Kennedy": Leon's line

                "Ada Wong": Ada's line

            """
    }
    ]
    
)

print(completion.choices[0].message.content)