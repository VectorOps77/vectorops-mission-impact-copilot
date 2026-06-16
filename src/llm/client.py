import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_openai(prompt: str) -> str:
    """
    Sends a prompt to OpenAI and returns the model response.
    """

    if not OPENAI_API_KEY:
        return "Error: OPENAI_API_KEY is missing. Add it to your .env file."

    response = client.responses.create(
        model=MODEL_NAME,
        instructions=(
            "You are a senior Technical Program Manager, DevSecOps advisor, "
            "and project reporting specialist. You help convert raw project activity "
            "into outcome-focused, measurable, executive-ready reporting. "
            "Do not invent facts, metrics, or customer feedback. "
            "If information is missing, clearly state what is missing."
        ),
        input=prompt,
    )

    return response.output_text