# Generated by Django 4.1.2 on 2022-11-16 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0006_messages_message_from'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='user',
            new_name='provider',
        ),
    ]
