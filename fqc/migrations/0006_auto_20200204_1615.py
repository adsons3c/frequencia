# Generated by Django 3.0 on 2020-02-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fqc', '0005_auto_20200204_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia_agentes',
            name='horario_entrada',
            field=models.TimeField(),
        ),
    ]
