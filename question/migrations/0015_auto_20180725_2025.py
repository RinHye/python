# Generated by Django 2.0.5 on 2018-07-25 20:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0014_auto_20180725_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('mail', models.CharField(max_length=100, verbose_name='Mail')),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(15)], verbose_name='Age')),
                ('sexe', models.CharField(choices=[('F', 'Femme'), ('M', 'Homme'), ('A', 'Ambigu')], max_length=5, verbose_name='Sexe')),
                ('interesse_par', models.CharField(choices=[('F', 'Femme'), ('M', 'Homme'), ('T', 'Tout')], max_length=5, verbose_name='Interessé par ')),
                ('tranche_age', models.CharField(choices=[('10', 'dizaine'), ('20', 'vingtaine'), ('30', 'trentaine'), ('40', 'quarantaine'), ('50', 'cinquantaine'), ('60', 'soixantaine'), ('70', 'soixante-dizaine'), ('80', 'quatre-vingtaine'), ('90', 'quatre-vingt-dizaine')], max_length=20, verbose_name="Tranche d'âge recherchée")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'utilisateur',
            },
        ),
        migrations.AlterField(
            model_name='choix',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.UserExtra'),
        ),
    ]
