# Generated by Django 4.1.2 on 2022-11-14 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0015_remove_timesheet_weekday_alter_timesheet_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
