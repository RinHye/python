# Generated by Django 2.0.5 on 2018-05-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_user_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.CharField(max_length=100, verbose_name='Mail'),
        ),
    ]
