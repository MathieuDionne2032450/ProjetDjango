# Generated by Django 4.2.6 on 2023-11-12 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boutique', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='date_debut',
            field=models.DateTimeField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='date_fin',
            field=models.DateTimeField(),
        ),
    ]
