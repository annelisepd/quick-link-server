from django.contrib import admin
from .models import *

# Register your models here.

class RedirectAdmin(admin.ModelAdmin):
    list_display = ["key", "url","access_count"]

    def access_count(self, obj):
        return obj.access_count()

class AccessAdmin(admin.ModelAdmin):
    list_display = ["creation", "ip","user_agent","redirect"]

admin.site.register(Redirect,RedirectAdmin)
admin.site.register(Access,AccessAdmin)