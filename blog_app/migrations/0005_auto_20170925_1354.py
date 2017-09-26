# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_comment_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='visit_time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
