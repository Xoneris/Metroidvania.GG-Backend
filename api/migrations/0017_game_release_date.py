# Generated by Django 5.0.2 on 2024-03-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_game_discord'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.DateField(blank=True, default='2024-01-01'),
        ),
    ]
