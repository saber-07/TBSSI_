# Generated by Django 3.2.11 on 2022-05-31 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Graphe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('Barres horizontales', 'Barres horizontales'), ('Barres Verticales', 'Barres Verticales'), ('Lineaire', 'Lineaire'), ('Camembert', 'Camembert'), ('Beignet', 'Beignet')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Indicateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Intitule_Indicateur', models.CharField(max_length=100, unique=True)),
                ('Objectif', models.CharField(default='objectif', max_length=100)),
                ('Domaine', models.CharField(default='Sécurité des RH', max_length=100)),
                ('Type', models.CharField(choices=[('IPP', 'Indicateurs de performance de productivité'), ('IPQ', 'Indicateurs de performance de qualité'), ('IPC', 'Indicateurs de performance de capacité'), ('IPS', 'Indicateurs de performance stratégiques')], default='IPS', max_length=50)),
                ('Methode_calcul', models.CharField(default='Nb utilisateur', max_length=200)),
                ('Periodicite', models.CharField(choices=[('Annuelle', 'Annuelle'), ('Mensuelle', 'Mensuelle')], max_length=100)),
                ('Source', models.CharField(default='DSSI', max_length=100)),
                ('validation_chef_dep', models.BooleanField(default=False)),
                ('validation_directeur', models.BooleanField(default=False)),
                ('Id_Graphe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.graphe')),
            ],
        ),
        migrations.CreateModel(
            name='TB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Intitule', models.CharField(max_length=200, unique=True)),
                ('Objectif', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interpretation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contenu', models.TextField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('Id_Indicateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.indicateur')),
            ],
        ),
        migrations.AddField(
            model_name='indicateur',
            name='Id_TB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tb'),
        ),
        migrations.AddField(
            model_name='indicateur',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Donnee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Valeur', models.IntegerField()),
                ('Id_Indicateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.indicateur')),
            ],
        ),
    ]
