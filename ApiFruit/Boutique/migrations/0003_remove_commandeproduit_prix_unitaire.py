# Generated by Django 4.2.6 on 2023-12-12 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boutique', '0002_commandeproduit_prix_unitaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commandeproduit',
            name='prix_unitaire',
        ),
    ]