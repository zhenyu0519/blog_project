# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20170922_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(blank=True, to='blog_app.Comment', null=True),
        ),
    ]
