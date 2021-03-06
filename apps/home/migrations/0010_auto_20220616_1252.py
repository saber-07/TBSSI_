# Generated by Django 3.2.11 on 2022-06-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220615_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicateur',
            name='Domaine',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indicateur',
            name='Methode_calcul',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='indicateur',
            name='Objectif',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indicateur',
            name='Source',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indicateur',
            name='Type',
            field=models.CharField(choices=[('IPP', 'Indicateurs de performance de productivité'), ('IPQ', 'Indicateurs de performance de qualité'), ('IPC', 'Indicateurs de performance de capacité'), ('IPS', 'Indicateurs de performance stratégiques')], max_length=50),
        ),
    ]
