# Generated by Django 4.1.5 on 2024-03-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='Beskriv',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='Beskrivelse',
            field=models.TextField(blank=True),
        ),
    ]