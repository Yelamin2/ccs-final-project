# Generated by Django 4.1.2 on 2022-11-15 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visits', '0020_rename_customer_timesheet_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_visit', models.DateTimeField()),
                ('end_visit', models.DateTimeField()),
                ('notes', models.TextField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_log', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_log', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]