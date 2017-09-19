# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('content', models.CharField(max_length=10000)),
                ('author', models.CharField(max_length=50)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('visit_time', models.IntegerField()),
                ('article_image', models.ImageField(max_length=2000, null=True, upload_to=b'image/%Y%m', blank=True)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
                ('index_order', models.IntegerField(default=999)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(to='blog_app.Article', max_length=50)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(to='blog_app.Category'),
        ),
    ]
