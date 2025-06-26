import pytest
from chat.food_classifiers.gpt_classifier import GPTFoodClassifier

class TestGPTFoodClassifier:
    @pytest.fixture
    def classifier(self):
        return GPTFoodClassifier()

    def test_analyze_meat_detection(self, classifier):
        result = classifier._analyze(["egg", "rice"])
        assert result['is_vegan'] is False
        assert result['is_vegetarian'] is True

    def test_is_vegetarian_or_vegan_true(self, classifier):
        assert classifier.is_vegetarian_or_vegan(["tofu", "rice", "egg"]) is True

    def test_is_vegetarian_or_vegan_false(self, classifier):
        assert classifier.is_vegetarian_or_vegan(["beef", "rice"]) is False