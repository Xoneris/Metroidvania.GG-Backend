# Generated by Django 5.0.2 on 2024-03-15 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_game_release_window'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='kickstarter_live',
        ),
        migrations.RemoveField(
            model_name='game',
            name='kickstarter_upcoming',
        ),
        migrations.AddField(
            model_name='game',
            name='kickstarter_status',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
