# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0007_auto_20150212_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default=b'null', max_length=200, verbose_name=b'director'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='movies', verbose_name=b'Genre', to='api_core.Genre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_score',
            field=models.FloatField(default=0, verbose_name=b'IMDB Score'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity_99',
            field=models.FloatField(default=0, verbose_name=b'99Popularity'),
            preserve_default=True,
        ),
    ]
