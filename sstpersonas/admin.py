from django.contrib import admin
from .models import PersonasSST

class PersonasSSTAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.creado_por:
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)

admin.site.register(PersonasSST, PersonasSSTAdmin)
