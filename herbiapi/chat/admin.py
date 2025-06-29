from django.contrib import admin
from .models import SimulatedConversation
from django.core.management import call_command

# Register your models here.

class SimulatedConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'foods', 'is_veg', 'created_at']
    actions = ['simulate_conversations']

    def simulate_conversations(self, request, queryset):
        call_command('simulate', 100, threads=50)
        self.message_user(request, 'Simulated conversations successfully.')


admin.site.register(SimulatedConversation, SimulatedConversationAdmin)
