from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.
from .models import SimulatedConversation
from .serializers import SimulatedConversationSerializer


class VegetarianOrVeganConversationsView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SimulatedConversationSerializer

    def get_queryset(self):
        return SimulatedConversation.objects.filter(is_veg=True)
