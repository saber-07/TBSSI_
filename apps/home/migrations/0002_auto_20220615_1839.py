# Generated by Django 3.2.11 on 2022-06-15 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donnee',
            old_name='indicateur',
            new_name='Id_Indicateur',
        ),
        migrations.RenameField(
            model_name='indicateur',
            old_name='graphe',
            new_name='Id_Graphe',
        ),
        migrations.RenameField(
            model_name='indicateur',
            old_name='tb',
            new_name='Id_TB',
        ),
        migrations.RenameField(
            model_name='interpretation',
            old_name='indicateur',
            new_name='Id_Indicateur',
        ),
    ]
