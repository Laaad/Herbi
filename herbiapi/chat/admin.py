from django.contrib import admin
from .models import SimulatedConversation

# Register your models here.

class SimulatedConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'foods', 'is_veg', 'created_at']

admin.site.register(SimulatedConversation, SimulatedConversationAdmin)
