# Generated by Django 4.1.1 on 2023-02-10 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher_App', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
