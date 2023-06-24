from django.contrib import admin
from .models import Ward, LGA, Announced_LGA_Results, Announced_PU_Results, Announced_State_Results, Announced_Ward_Results, AgentName, States, Party, Polling_Unit

# Register your models here.

admin.site.register(Ward)
admin.site.register(LGA)
admin.site.register(States)
admin.site.register(Announced_LGA_Results)
admin.site.register(Announced_PU_Results)
admin.site.register(Announced_State_Results)
admin.site.register(Announced_Ward_Results)
admin.site.register(Party)
admin.site.register(Polling_Unit)
admin.site.register(AgentName)
