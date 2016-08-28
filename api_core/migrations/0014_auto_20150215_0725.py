# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0013_auto_20150215_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set([('name', 'director')]),
        ),
    ]
