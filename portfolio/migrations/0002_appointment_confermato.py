# Generated by Django 5.1.4 on 2025-02-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='confermato',
            field=models.BooleanField(default=False),
        ),
    ]
