from rest_framework import generics, permissions, authentication

# Create your views here.
from .models import SimulatedConversation
from .serializers import SimulatedConversationSerializer


class VegetarianOrVeganConversationsView(generics.ListAPIView):
    """
    View to list the result of all conversations classified as vegetarian or vegan providing the foods lists.
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SimulatedConversationSerializer

    def get_queryset(self):
        return SimulatedConversation.objects.filter(is_veg=True)
