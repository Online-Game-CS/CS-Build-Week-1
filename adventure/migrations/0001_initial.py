# Generated by Django 3.0.3 on 2020-03-03 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.IntegerField(default=0)),
                ('j', models.IntegerField(default=0)),
                ('n_to', models.IntegerField(default=0)),
                ('s_to', models.IntegerField(default=0)),
                ('e_to', models.IntegerField(default=0)),
                ('w_to', models.IntegerField(default=0)),
                ('wall', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentRoom', models.IntegerField(default=0)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
