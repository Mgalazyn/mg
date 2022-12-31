from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.TextField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['created']


class PartLife(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    short_intro = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(null=True, blank=True, upload_to='', default='')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)

    def __str_(self) -> str:
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    receiver = models.EmailField(default='mgalazynn@gmail.com')
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject

