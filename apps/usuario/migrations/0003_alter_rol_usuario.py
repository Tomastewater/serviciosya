# Generated by Django 5.1.1 on 2024-10-22 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_usuario_rol_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rols', to='usuario.usuario'),
        ),
    ]