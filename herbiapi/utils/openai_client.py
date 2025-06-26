from openai import OpenAI
from llm_interface import LLMInterface
from typing import Any

class OpenAILLM(LLMInterface):
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def ask(self, prompt: str, role: str = "user", **kwargs: Any) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": role, "content": prompt}],
            **kwargs
        )
        reply = response.choices[0].message["content"].strip()

        return reply