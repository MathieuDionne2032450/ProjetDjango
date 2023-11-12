
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='img/')),
            ],
        ),
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
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commander', models.DateTimeField(null=True)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='CommandeClient', to='Boutique.client', validators=[django.core.validators.MinValueValidator(0, "L'id doit etre superrieur a 0")])),
                ('produit', models.ManyToManyField(to='Boutique.produit')),
            ],
        ),
    ]
