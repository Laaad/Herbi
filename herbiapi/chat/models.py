from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SimulatedConversation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="The user who owns this simulated conversation.",
        null=True,
        blank=True
    )
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
    
