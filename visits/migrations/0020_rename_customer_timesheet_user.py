# Generated by Django 4.1.2 on 2022-11-15 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0019_rename_user_timesheet_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timesheet',
            old_name='customer',
            new_name='user',
        ),
    ]