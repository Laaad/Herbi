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
            "Extract exactly 3 food names from the following text: "
            f"{foods}\n\n"
            "You must return exactly 3 food names separated by commas. "
            "If there are more than 3 foods mentioned, select the first 3. "
            "Only list the food names, no additional comments or explanations. "
            "Respond ONLY with a valid text object, no explanation or text outside the list."
        )

        text = self.llm.ask(full_prompt, role="system")
        
        food_list = [food.strip() for food in text.split(",") if food.strip()]
        if len(food_list) > 3:
            food_list = food_list[:3]
        return food_list

    def _analyze(self, foods) -> dict:
        prompt = (
        f"You are a strict food classification expert. Carefully evaluate whether each of the following foods is vegetarian and/or vegan: {foods}.\n\n"
        "For each food, verify the typical ingredients. Do not assume they are vegetarian or vegan without justification. "
        "If a food typically contains meat, fish, eggs, dairy, or any other animal products, it may not be vegan or vegetarian.\n\n"
        "Assume this is a legal classification: if you incorrectly classify a non-vegan or non-vegetarian food as vegan/vegetarian, "
        "you may be fined or punished. Be absolutely certain in your classification.\n\n"
        "After analyzing all 3 foods individually, provide a FINAL verdict:\n"
        "- is_vegetarian is true ONLY if all 3 foods are vegetarian.\n"
        "- is_vegan is true ONLY if all 3 foods are vegan.\n\n"
        "Respond ONLY with a JSON object like this:\n"
        '{\n'
        '  "is_vegetarian": true or false,\n'
        '  "is_vegan": true or false\n'
        '}\n\n'
        "Do not include any other text. Do not explain. Only return valid JSON."
        )
        response = self.llm.ask(prompt=prompt, role="system")
        
        try:
            result = json.loads(response.replace("'", "\""))
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
