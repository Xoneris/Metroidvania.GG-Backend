# Generated by Django 5.0.2 on 2024-02-07 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('developer', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
    ]
