# Generated by Django 5.0.2 on 2024-03-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_game_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='release',
            field=models.CharField(default='0', max_length=100),
        ),
    ]