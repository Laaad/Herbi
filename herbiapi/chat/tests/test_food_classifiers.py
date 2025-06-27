import pytest
from chat.food_classifiers.llm_classifier import LLMFoodClassifier
from utils.openai_client import OpenAILLM
from core.settings.base import OPENAI_API_KEY

class TestLLMFoodClassifier:
    @pytest.fixture
    def classifier(self):
        openai_client = OpenAILLM(api_key=OPENAI_API_KEY)
        return LLMFoodClassifier(llm=openai_client)

    def test_analyze_meat_detection(self, classifier):
        result = classifier._analyze(["egg", "rice"])
        assert result['is_vegan'] is False
        assert result['is_vegetarian'] is True

    def test_is_vegetarian_or_vegan_true(self, classifier):
        assert classifier.is_vegetarian_or_vegan(["tofu", "rice", "egg"]) is True

    def test_is_vegetarian_or_vegan_false(self, classifier):
        assert classifier.is_vegetarian_or_vegan(["beef", "rice"]) is False