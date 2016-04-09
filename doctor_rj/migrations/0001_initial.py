# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=2, verbose_name='C\xf3digo da Esfera Administrativa')),
                ('name', models.CharField(max_length=60, verbose_name='Esfera Administrativa')),
            ],
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnes', models.CharField(max_length=7)),
                ('cnpj', models.CharField(max_length=14)),
                ('company_name', models.CharField(max_length=60)),
                ('common_name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=10)),
                ('add_address', models.CharField(max_length=60)),
                ('district', models.CharField(max_length=60)),
                ('cep', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=60)),
                ('fax', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('latitude', models.CharField(max_length=60)),
                ('longitude', models.CharField(max_length=60)),
                ('coordinates_update', models.CharField(max_length=60, null=True, blank=True)),
                ('administrative', models.ForeignKey(to='doctor_rj.Administrative')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationNature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=2, verbose_name='C\xf3digo da Natureza da Organiza\xe7\xe3o')),
                ('nature', models.CharField(max_length=60, verbose_name='Natureza da Organiza\xe7\xe3o')),
            ],
        ),
        migrations.CreateModel(
            name='TeachingActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=2, verbose_name='C\xf3digo da Atividade de Ensino')),
                ('activity_type', models.CharField(max_length=60, verbose_name='Atividade de Ensino')),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=2, verbose_name='C\xf3digo do Tipo da Unidade')),
                ('name', models.CharField(max_length=60, verbose_name=b'Tipo de Estabelecimento')),
            ],
        ),
        migrations.AddField(
            model_name='establishment',
            name='organization_nature',
            field=models.ForeignKey(to='doctor_rj.OrganizationNature'),
        ),
        migrations.AddField(
            model_name='establishment',
            name='teaching_activity',
            field=models.ForeignKey(to='doctor_rj.TeachingActivity'),
        ),
        migrations.AddField(
            model_name='establishment',
            name='unit_type',
            field=models.ForeignKey(to='doctor_rj.UnitType'),
        ),
    ]
