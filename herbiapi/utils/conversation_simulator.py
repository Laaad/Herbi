from utils.llm_interface import LLMInterface

class ConversationSimulator:
    def __init__(self, asker: LLMInterface, responder: LLMInterface):
        self._asker = asker
        self._responder = responder
        self.question = None
        self.answer = None

    def converse(self, open_question, open_answer):
        self.question = self._asker.ask(prompt=open_question, role="user")
        open_answer+= f"You answer the question: {self.question}"
        self.answer = self._responder.ask(prompt=open_answer, role="user")
        return self

