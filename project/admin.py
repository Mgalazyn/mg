from django.contrib import admin

# Register your models here.
from .models import Project, PartLife

admin.site.register(Project)
admin.site.register(PartLife)