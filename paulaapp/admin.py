from django.contrib import admin
from .models import Prospect


class ProspectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Prospect, ProspectAdmin)
# Register your models here.
