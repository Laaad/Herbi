from .base import FoodClassifier
from utils.llm_interface import LLMInterface
import json

class LLMFoodClassifier(FoodClassifier):
    def __init__(self, llm: LLMInterface):
        self.llm = llm

    def extract_foods(self, foods: str) -> list[str]:
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
        return food_list[:3]

    def _analyze(self, food: str) -> dict:
        prompt = (
            f"You are a strict food classification expert. Carefully evaluate whether the following food is vegetarian and/or vegan: {food}.\n\n"
            "Follow these rules:\n\n"
            "- Use common **Western dietary definitions**:\n"
            "  - Vegetarian: no meat, poultry, fish, or animal-derived ingredients that involve animal slaughter. **Eggs and dairy are allowed** (lacto-ovo vegetarian).\n"
            "  - Vegan: no meat, poultry, fish, dairy, eggs, honey, gelatin, or any other animal-derived ingredients or by-products.\n\n"
            "- Do not assume a food is vegetarian or vegan unless you are confident in its typical ingredients.\n\n"
            "- If the food typically contains any non-vegetarian or non-vegan ingredients, even optionally, classify it accordingly (i.e., err on the side of caution).\n\n"
            "Assume this is a legal classification: if you incorrectly classify a non-vegan or non-vegetarian food as vegan/vegetarian, you may be fined or punished. Be absolutely certain in your classification.\n\n"
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

    def is_vegetarian_or_vegan(self, foods: list[str]) -> bool:
        """
        Returns True only if ALL foods are at least vegetarian or vegan.
        """
        for food in foods:
            result = self._analyze(food)
            if not (result["is_vegetarian"] or result["is_vegan"]):
                return False
        return True

