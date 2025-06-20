from django.db import models

# Create your models here.

class SimulatedConversation(models.Model):
    response_text = models.TextField()
    foods = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
