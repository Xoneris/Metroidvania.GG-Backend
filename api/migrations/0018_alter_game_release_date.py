# Generated by Django 5.0.2 on 2024-03-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_game_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(blank=True),
        ),
    ]
