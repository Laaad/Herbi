from abc import ABC, abstractmethod


class FoodClassifier(ABC):
    @abstractmethod
    def _analyze(self, foods: list[str]) -> dict:
        """Takes a list of foods and returns a dictionary of boolean flags for food categories"""
        pass

    @abstractmethod
    def is_vegetarian_or_vegan(self, foods: list[str]) -> bool:
        """ Takes a list of foods and returns a boolean indicating is list is vegetarian or vegan"""
        pass

    @abstractmethod
    def extract_foods(self, foods: str) -> list[str]:
        """Takes a string, extracts food names and returns a list of foods"""
        pass