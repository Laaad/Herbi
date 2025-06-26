from .base import FoodClassifier
from openai import OpenAI
import json
from core.settings.base import OPENAI_API_KEY

class GPTFoodClassifier(FoodClassifier):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def _analyze(self, foods) -> dict:
        prompt = (
            f'Given the following list of foods: {foods}, classify whether the person is vegetarian and/or vegan.'
            'Return only a JSON object in this format:'
            '{"is_vegetarian": true or false, "is_vegan": true or false}'
            'Respond ONLY with a valid text object, no explanation or text outside the JSON.'
        )

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        content = response.choices[0].message.content.strip()
        try:
            result = json.loads(content.replace("'", "'"))
        except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON response from OpenAI: {content}")

        if not all(k in result for k in ("is_vegetarian", "is_vegan")):
                raise ValueError("Missing expected keys in response")
        if not isinstance(result["is_vegetarian"], bool) or not isinstance(result["is_vegan"], bool):
                raise ValueError("Values must be boolean")

        return result

    def is_vegetarian_or_vegan(self, foods) -> bool:
        """Takes a list of foods and returns a boolean indicating if the list is vegetarian or vegan"""
        result = self._analyze(foods)
        return result["is_vegetarian"] or result["is_vegan"]