# Generated by Django 5.1.2 on 2024-10-22 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='departamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]