# Generated by Django 5.0.2 on 2024-02-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_game_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='release',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
