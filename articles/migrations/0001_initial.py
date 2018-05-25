# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Загаловок', max_length=40)),
                ('text', models.TextField(verbose_name='Текст статьи', blank=True)),
                ('image', models.ImageField(blank=True, upload_to='static/img')),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.AlterIndexTogether(
            name='article',
            index_together=set([('id', 'slug')]),
        ),
    ]
