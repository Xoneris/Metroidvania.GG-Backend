# Generated by Django 5.0.2 on 2024-03-01 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_game_release_remove_game_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='release_window',
            new_name='release',
        ),
    ]
