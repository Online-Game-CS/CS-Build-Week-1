# Generated by Django 3.0.3 on 2020-03-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.CharField(default='DEFAULT DESCRIPTION', max_length=500),
        ),
        migrations.AddField(
            model_name='room',
            name='title',
            field=models.CharField(default='DEFAULT TITLE', max_length=50),
        ),
    ]
