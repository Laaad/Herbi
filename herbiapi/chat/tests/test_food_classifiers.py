import pytest
from chat.food_classifiers.llm_classifier import LLMFoodClassifier
from utils.openai_client import OpenAILLM
from core.settings import OPENAI_API_KEY

class TestLLMFoodClassifier:
    @pytest.fixture
    def classifier(self):
        openai_client = OpenAILLM(api_key=OPENAI_API_KEY)
        return LLMFoodClassifier(llm=openai_client)

    def test_analyze(self, classifier):
        result1 = classifier._analyze("egg")
        assert result1['is_vegan'] is False
        assert result1['is_vegetarian'] is True
        result2 = classifier._analyze("tofu")
        assert result2['is_vegan'] is True
        assert result2['is_vegetarian'] is True


    def test_is_vegetarian_or_vegan_true(self, classifier):
        assert classifier.is_vegetarian_or_vegan(["tofu", "rice", "egg"]) is True

    def test_is_vegetarian_or_vegan_false(self, classifier):
        assert classifier.is_vegetarian_or_vegan(["beef", "rice"]) is False