# Generated by Django 3.2.11 on 2022-06-04 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_customuser_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sexe',
            field=models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], default='Masculin', max_length=10),
        ),
    ]