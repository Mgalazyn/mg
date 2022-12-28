from django.contrib import admin

# Register your models here.
from .models import Project, PartLife, Message

admin.site.register(Project)
admin.site.register(PartLife)
admin.site.register(Message)