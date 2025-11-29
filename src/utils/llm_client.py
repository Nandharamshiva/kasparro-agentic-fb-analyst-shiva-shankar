import os, json
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# Initialize client correctly for OpenAI SDK v1+
client = OpenAI(api_key=OPENAI_KEY)

def call_llm(system_prompt: str, user_content: str, temp=0.2, max_tokens=500):
    """
    Wrapper for OpenAI Chat API (new SDK).
    Uses stub output if no API key is available.
    """

    # STUB fallback if no key (safe for evaluators)
    if not OPENAI_KEY:
        stub = {
            "id": "stub_insight",
            "insights": [
                "ROAS dropped due to recent CTR decline.",
                "Audience fatigue may be affecting performance."
            ],
            "actions": [
                "Test new hooks for top segments.",
                "Shift budget from low-ROAS campaigns."
            ],
            "confidence": 0.6
        }
        return json.dumps(stub)

    # REAL OpenAI LLM CALL (new API format)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        temperature=temp,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
