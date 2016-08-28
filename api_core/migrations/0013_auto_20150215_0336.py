# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0012_auto_20150215_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='movies', verbose_name=b'Genre', to='api_core.Genre'),
            preserve_default=True,
        ),
    ]
