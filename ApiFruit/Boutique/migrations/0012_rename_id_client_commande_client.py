# Generated by Django 4.2.6 on 2023-11-09 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boutique', '0011_alter_commande_id_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='id_client',
            new_name='client',
        ),
    ]
