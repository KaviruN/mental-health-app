# Generated by Django 5.1.3 on 2024-12-10 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aichat', '0006_alter_chatdata_options_alter_chatdata_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatdata',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='chatdata',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]