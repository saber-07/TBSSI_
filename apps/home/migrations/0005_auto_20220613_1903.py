# Generated by Django 3.2.11 on 2022-06-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_tb_validation_rapport'),
    ]

    operations = [
        migrations.AddField(
            model_name='donnee',
            name='validation_chef_dep',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donnee',
            name='validation_directeur',
            field=models.BooleanField(default=False),
        ),
    ]
