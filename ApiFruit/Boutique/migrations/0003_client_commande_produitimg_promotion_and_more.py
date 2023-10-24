# Generated by Django 4.2.6 on 2023-10-24 14:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boutique', '0002_alter_produit_quantite_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=255)),
                ('prenom_client', models.CharField(max_length=255)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('courriel', models.CharField(max_length=255)),
                ('num_telephone', models.CharField(max_length=255, null=True)),
                ('date_inscription', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commander', models.BooleanField(default=False)),
                ('dateCommander', models.DateTimeField(null=True)),
                ('id_client', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, "L'id doit etre superrieur a 0")])),
            ],
        ),
        migrations.CreateModel(
            name='ProduitImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_produit', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, "L'id doit etre superieur a 0")])),
                ('path', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_rabais', models.CharField(max_length=255)),
                ('valeur', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'La valeur doit etre superieur a 0')])),
                ('description_promotion', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='produit',
            name='description_produit',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='id_categorie',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, "L'id doit etre superrieur a 0")]),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0, 'Le prix doit etre superrieur a 0')]),
        ),
        migrations.AlterField(
            model_name='produit',
            name='quantite_stock',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, 'La quantite doit etre superrieur a 0')]),
        ),
    ]
