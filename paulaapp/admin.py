from django.contrib import admin
from .models import Prospect
from .models import Document


class ProspectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Prospect, ProspectAdmin)
admin.site.register(Document, ProspectAdmin)
# Register your models here.
