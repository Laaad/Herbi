from .base import FoodClassifier
from utils.llm_interface import LLMInterface
import json

class LLMFoodClassifier(FoodClassifier):
    def __init__(self, llm: LLMInterface):
          self.llm = llm

    def extract_foods(self, foods: str) -> list[str]:
        """
        Entry point: extract foods using appropriate internal strategy.
        For now, it only supports _gpt_get_foods.
        """
        full_prompt = (
            "Extract the food names from the following text: "
            f"{foods}"
            "You always respond in a structured, list of food names with a comma separator. "
            "Only list the food names, no additional comments or explanations."
            "Respond ONLY with a valid text object, no explanation or text outside the list."
        )

        text = self.llm.ask(full_prompt, role="user", temperature=0.9)

        return text.split(",")

    def _analyze(self, foods) -> dict:
        prompt = (
            f'Given the following list of foods: {foods}, classify whether the person is vegetarian and/or vegan.'
            'Make sure check the ingredients of the foods mentioned and whether they are vegetarian or vegan. Always check the ingredients.'
            'If the person is not vegetarian or vegan, return false for both is_vegetarian and is_vegan.'
            'Return only a JSON object in this format:'
            '{"is_vegetarian": true or false, "is_vegan": true or false}'
            'Respond ONLY with a valid text object, no explanation or text outside the JSON.'
        )
        response = self.llm.ask(prompt=prompt)
        
        try:
            result = json.loads(response.replace("'", "'"))
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON response: {response}")

        if not all(k in result for k in ("is_vegetarian", "is_vegan")):
            raise ValueError("Missing expected keys in response")
        if not isinstance(result["is_vegetarian"], bool) or not isinstance(result["is_vegan"], bool):
            raise ValueError("Values must be boolean")

        return result

    def is_vegetarian_or_vegan(self, foods) -> bool:
        """Takes a list of foods and returns a boolean indicating if the list is vegetarian or vegan"""
        result = self._analyze(foods)
        return result["is_vegetarian"] or result["is_vegan"]
