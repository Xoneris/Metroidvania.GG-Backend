# Generated by Django 5.0.2 on 2024-03-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_game_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='kickstarter_page',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
