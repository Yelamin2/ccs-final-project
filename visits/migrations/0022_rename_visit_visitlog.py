# Generated by Django 4.1.2 on 2022-11-15 14:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visits', '0021_visit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visit',
            new_name='VisitLog',
        ),
    ]
