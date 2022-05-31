# Generated by Django 3.2.11 on 2022-05-30 20:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_indicateur_validation_directeur'),
    ]

    operations = [
        migrations.AddField(
            model_name='interpretation',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='indicateur',
            name='Periodicite',
            field=models.CharField(choices=[('Annuelle', 'Annuelle'), ('Mensuelle', 'Mensuelle')], max_length=100),
        ),
    ]
