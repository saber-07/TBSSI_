# Generated by Django 3.2.11 on 2022-06-02 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_direction_directeur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='directeur',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
