# Generated by Django 3.2.11 on 2022-06-13 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0008_auto_20220613_1419'),
        ('home', '0003_auto_20220609_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonneeMesure',
            fields=[
                ('donnee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.donnee')),
                ('mesure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.mesure')),
            ],
            bases=('home.donnee',),
        ),
        migrations.CreateModel(
            name='DonneeFilliale',
            fields=[
                ('donnee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.donnee')),
                ('filiale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.filiale')),
            ],
            bases=('home.donnee',),
        ),
        migrations.CreateModel(
            name='DonneeApplication',
            fields=[
                ('donnee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.donnee')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.application')),
            ],
            bases=('home.donnee',),
        ),
    ]
