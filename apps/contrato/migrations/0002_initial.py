# Generated by Django 5.1.1 on 2025-06-22 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consumidor', '0001_initial'),
        ('contrato', '0001_initial'),
        ('facturacion', '0002_initial'),
        ('servicio', '0001_initial'),
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='direccion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ubicacion.direccion'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contratos', to='facturacion.factura'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='servicio_prestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.servicioprestado'),
        ),
        migrations.AddField(
            model_name='solicitudservicio',
            name='consumidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumidor.consumidor'),
        ),
        migrations.AddField(
            model_name='solicitudservicio',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.direccion'),
        ),
        migrations.AddField(
            model_name='solicitudservicio',
            name='servicio_prestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.servicioprestado'),
        ),
    ]
