from django.urls import path
from chat.views import VegetarianOrVeganConversationsView

app_name = 'chat'

urlpatterns = [
    path('', VegetarianOrVeganConversationsView.as_view(), name='veg-conversations'),
] 