# Generated by Django 5.1.1 on 2024-10-19 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0001_initial'),
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.factura'),
        ),
    ]