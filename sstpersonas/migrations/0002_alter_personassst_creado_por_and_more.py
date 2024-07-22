# Generated by Django 4.1.2 on 2024-07-22 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0001_initial'),
        ('sstpersonas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personassst',
            name='creado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creado por'),
        ),
        migrations.AlterField(
            model_name='personassst',
            name='persona_SST',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.persona'),
        ),
    ]
