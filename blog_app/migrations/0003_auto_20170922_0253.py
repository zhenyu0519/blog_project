# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20170918_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.URLField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(max_length=2000, null=True, upload_to=b'post_image/%Y%m%d', blank=True),
        ),
    ]
