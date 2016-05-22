from django.contrib import admin

from .models import Provider, API, Logic

admin.site.register(Provider)
admin.site.register(API)
admin.site.register(Logic)
