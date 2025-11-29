import os
from openai import OpenAI
from dotenv import load_dotenv
from loguru import logger
import json

from app.tools import get_weather

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FUNCTIONS = {
    "get_weather": get_weather
}

function_descriptions = [
    {
        "name": "get_weather",
        "description": "Get current weather in a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
]

class Agent:
    def run(self, prompt: str):

        logger.info(f"User prompt: {prompt}")

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            functions=function_descriptions,
            function_call="auto"
        )

        msg = response.choices[0].message

        # If model wants to call a function
        if msg.function_call:
            fn_name = msg.function_call.name
            arguments = json.loads(msg.function_call.arguments)

            logger.info(f"AI is calling function: {fn_name} with args: {arguments}")

            fn = FUNCTIONS.get(fn_name)
            result = fn(**arguments)

            return {"function_result": result}

        # Normal text response
        return {"response": msg.content}