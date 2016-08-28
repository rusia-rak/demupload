# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0006_auto_20150212_0824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_name',
            new_name='name',
        ),
    ]
