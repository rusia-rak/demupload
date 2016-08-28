# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0003_auto_20150210_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity_99',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
