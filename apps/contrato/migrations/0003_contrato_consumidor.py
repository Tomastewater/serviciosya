# Generated by Django 5.1.1 on 2024-11-23 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumidor', '0002_initial'),
        ('contrato', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='consumidor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contratos', to='consumidor.consumidor'),
        ),
    ]