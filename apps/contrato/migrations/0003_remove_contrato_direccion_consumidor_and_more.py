# Generated by Django 5.1.1 on 2024-10-22 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0002_alter_contrato_factura'),
        ('facturacion', '0001_initial'),
        ('ubicacion', '0002_alter_direccion_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='direccion_consumidor',
        ),
        migrations.AddField(
            model_name='contrato',
            name='direccion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ubicacion.direccion'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contratos', to='facturacion.factura'),
        ),
    ]