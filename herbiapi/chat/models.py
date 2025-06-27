from django.db import models

# Create your models here.

class SimulatedConversation(models.Model):
    foods = models.JSONField(
        help_text="A list or dictionary of foods consumed. Expected to be a structured JSON object."
    )
    is_veg = models.BooleanField(
        help_text="Indicates whether the foods suggest a vegetarian or vegan diet. True if vegetarian/vegan, False otherwise."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when this simulated conversation was created."
    )

