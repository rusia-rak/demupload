# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.CharField(default=b'null', max_length=200),
            preserve_default=True,
        ),
    ]
