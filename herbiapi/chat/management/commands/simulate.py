import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from chat.food_classifiers.llm_classifier import LLMFoodClassifier
from chat.models import SimulatedConversation
from core.settings import OPENAI_API_KEY
from django.core.management.base import BaseCommand
from utils.conversation_simulator import ConversationSimulator
from utils.openai_client import OpenAILLM

model = OpenAILLM(api_key=OPENAI_API_KEY)
asker = OpenAILLM(api_key=OPENAI_API_KEY)
responder = OpenAILLM(api_key=OPENAI_API_KEY)
classifier = LLMFoodClassifier(llm=model)
conversation = ConversationSimulator(asker=asker, responder=responder)

class Command(BaseCommand):
    help = "Simulates N GPT food conversations"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Number of simulations to run")
        parser.add_argument("--threads", type=int, default=5, help="Thread count")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        threads = kwargs["threads"]
        self._simulate_n(count, threads)

    def _run_single_simulation(self):
        try:
            open_question = (
                "You are a chatbot designed to ask users about their favorite foods. "
                "Start by asking for their top three favorite foods. "
                "Only ask about their top three favorite foods, no other questions or comments."
            )
            open_answer = (
                "You are a food vlogger who is interested in specific, diverse dishes. "
                "You are designed to respond to questions about your top three favorite foods. "
                "When asked, you will dynamically and randomly generate a list of three distinct foods. "
                "Ensure variety in your responses each time you are asked. "
            )
            respond = conversation.converse(open_question=open_question, open_answer=open_answer)

            is_veg = classifier.is_vegetarian_or_vegan(respond.answer)
            foods = classifier.extract_foods(respond.answer)
            data = {"foods": foods, "is_veg": is_veg}
            SimulatedConversation.objects.create(**data)
            time.sleep(0.5)
        except Exception as e:
            print(f"[ERROR] Simulation failed: {e}")
            time.sleep(1)


    def _simulate_n(self, n: int = 100, threads: int = 100):
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(self._run_single_simulation) for _ in range(n)]
            time.sleep(0.4)
            for future in as_completed(futures):
                pass
