from django.urls import path
from chat.views import ConversationsView, VegetarianOrVeganConversationsView

app_name = 'chat'

urlpatterns = [
    path('', ConversationsView.as_view(), name='conversations'),
    path('vegs/', VegetarianOrVeganConversationsView.as_view(), name='vegs'),
] 