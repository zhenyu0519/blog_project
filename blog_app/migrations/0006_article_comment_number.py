# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20170925_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
