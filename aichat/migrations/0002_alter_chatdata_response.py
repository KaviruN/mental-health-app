# Generated by Django 5.1.3 on 2024-11-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aichat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatdata',
            name='response',
            field=models.TextField(max_length=10000),
        ),
    ]