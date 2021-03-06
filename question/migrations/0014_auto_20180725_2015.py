# Generated by Django 2.0.5 on 2018-07-25 20:15

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0013_auto_20180725_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='choix',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='choix',
            unique_together={('user', 'date')},
        ),
    ]
