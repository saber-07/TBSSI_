# Generated by Django 3.2.11 on 2022-06-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_filiale_pdg'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='sexe',
            field=models.CharField(blank=True, choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=10),
        ),
    ]
