from rest_framework import generics, permissions, authentication
from drf_spectacular.utils import extend_schema

# Create your views here.
from .models import SimulatedConversation
from .serializers import SimulatedConversationSerializer


@extend_schema(
    tags=["Conversations"],
    summary="List Vegetarian/Vegan Conversations",
    description="Retrieve all conversations that have been classified as vegetarian or vegan, providing food lists and classification details.",
)
class VegetarianOrVeganConversationsView(generics.ListAPIView):
    """
    View to list the result of all conversations classified as vegetarian or vegan providing the foods lists.
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SimulatedConversationSerializer

    def get_queryset(self):
        return SimulatedConversation.objects.filter(is_veg=True)
