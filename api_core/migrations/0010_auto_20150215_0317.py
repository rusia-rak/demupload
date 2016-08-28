# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0009_auto_20150215_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_score',
            field=models.FloatField(default=0, verbose_name=b'IMDB Score', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity_99',
            field=models.FloatField(default=0, verbose_name=b'99Popularity', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
            preserve_default=True,
        ),
    ]
