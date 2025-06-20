from django.contrib import admin
"""
This module registers the Topic and Entry models with the Django admin interface,
allowing them to be managed through the Django admin site.
"""


# Register your models here.

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
