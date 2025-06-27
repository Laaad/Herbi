from abc import ABC, abstractmethod
from typing import Any

class LLMInterface(ABC):
    @abstractmethod
    def ask(self, prompt: str, role: str = "user", **kwargs: Any) -> str:
        """
        Asks the LLM a question.

        Args:
            prompt (str): The content to send.
            role (str): The role of the message.
            **kwargs: Additional LLM-specific options like temperature, context, etc.

        Returns:
            str: The LLM's response.
        """
        pass
