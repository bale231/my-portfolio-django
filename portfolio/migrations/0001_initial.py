# Generated by Django 5.1.4 on 2025-02-17 11:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_paziente', models.CharField(max_length=255)),
                ('eta', models.IntegerField()),
                ('tipologia_visita', models.CharField(choices=[('Generale', 'Generale'), ('Specialistica', 'Specialistica')], max_length=100)),
                ('diagnosi', models.TextField(blank=True, null=True)),
                ('orario', models.TimeField()),
                ('numero_stanza', models.IntegerField()),
                ('dottore', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
