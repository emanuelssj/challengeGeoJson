# Generated by Django 2.2.1 on 2019-06-19 02:08

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partnersAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='address',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
        migrations.AlterField(
            model_name='partner',
            name='coverageArea',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
