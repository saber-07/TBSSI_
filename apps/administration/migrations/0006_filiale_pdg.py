# Generated by Django 3.2.11 on 2022-06-04 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_auto_20220602_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='filiale',
            name='pdg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
