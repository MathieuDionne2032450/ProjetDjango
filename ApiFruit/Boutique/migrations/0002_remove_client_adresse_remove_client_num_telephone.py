# Generated by Django 4.2.6 on 2023-11-16 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boutique', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='client',
            name='num_telephone',
        ),
    ]