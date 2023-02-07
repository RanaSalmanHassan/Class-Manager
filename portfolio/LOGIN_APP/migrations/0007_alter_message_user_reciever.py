# Generated by Django 4.1.1 on 2023-02-04 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN_APP', '0006_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user_reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_recipent', to=settings.AUTH_USER_MODEL),
        ),
    ]