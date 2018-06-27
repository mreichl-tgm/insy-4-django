# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strasse', models.CharField(max_length=255)),
                ('hnr', models.IntegerField()),
                ('plz', models.CharField(max_length=20)),
                ('ort', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Adressen',
            },
        ),
        migrations.CreateModel(
            name='Bestellung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('zuletzt_online', models.DateField(null=True)),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='bestellung',
            name='kunde',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Kunde'),
        ),
        migrations.AddField(
            model_name='adresse',
            name='land',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.Land'),
        ),
    ]