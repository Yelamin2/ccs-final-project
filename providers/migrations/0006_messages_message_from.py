# Generated by Django 4.1.2 on 2022-11-16 15:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0005_remove_invoice_visit_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message_from',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]