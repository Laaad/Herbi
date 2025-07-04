from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from drf_spectacular.utils import extend_schema
from .serializers import UserLoginSerializer, UserSerializer

# Create your views here.
@extend_schema(
    tags=["Authentication"],
    summary="User Login",
    description="Authenticate a user with username and password, then log them in.",
    request=UserLoginSerializer,
)
class LoginView(APIView):
    """Login view for user authentication."""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({
                'message': 'Login successful',
                'user': UserSerializer(user).data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)