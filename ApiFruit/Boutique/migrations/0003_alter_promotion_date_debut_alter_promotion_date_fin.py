# Generated by Django 4.2.6 on 2023-11-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boutique', '0002_alter_promotion_date_debut_alter_promotion_date_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='date_debut',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='date_fin',
            field=models.DateTimeField(null=True),
        ),
    ]
