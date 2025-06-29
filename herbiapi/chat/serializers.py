from rest_framework import serializers
from .models import SimulatedConversation

class SimulatedConversationSerializer(serializers.ModelSerializer[SimulatedConversation]):
    class Meta:
        model = SimulatedConversation
        fields = ['id', 'is_veg', 'foods', 'user']
