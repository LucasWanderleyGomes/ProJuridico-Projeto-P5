# Generated by Django 5.0.1 on 2025-03-10 22:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processo',
            options={'verbose_name': 'Processo', 'verbose_name_plural': 'Processos'},
        ),
        migrations.AddField(
            model_name='processo',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='atualizacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processo',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
