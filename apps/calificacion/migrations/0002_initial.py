# Generated by Django 5.1.1 on 2025-06-22 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calificacion', '0001_initial'),
        ('prestador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='prestador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calificaciones', to='prestador.prestador'),
        ),
    ]
