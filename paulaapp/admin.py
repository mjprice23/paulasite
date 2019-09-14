from django.contrib import admin
from .models import Prospect, Visit


class ProspectAdmin(admin.ModelAdmin):
    pass


class VisitAdmin(admin.ModelAdmin):
    pass


admin.site.register(Prospect, ProspectAdmin)
admin.site.register(Visit, VisitAdmin)
# Register your models here.
