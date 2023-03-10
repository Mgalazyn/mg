# Generated by Django 4.1.4 on 2022-12-17 18:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartLife',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('short_intro', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]
