# Generated by Django 3.0 on 2020-02-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fqc', '0004_auto_20200131_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia_agentes',
            name='horario_saida',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='frequencia_agentes',
            name='total_hora',
            field=models.TimeField(blank=True, null=True),
        ),
    ]