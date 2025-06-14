# Generated by Django 5.1.7 on 2025-06-02 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_calificacion', models.DateField()),
                ('calificacion', models.IntegerField(choices=[(1, '1 - Muy malo'), (2, '2 - Malo'), (3, '3 - Regular'), (4, '4 - Bueno'), (5, '5 - Excelente')])),
                ('comentario', models.TextField(max_length=1000)),
            ],
        ),
    ]
