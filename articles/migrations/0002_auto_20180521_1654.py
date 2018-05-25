# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(verbose_name='Загаловок', max_length=40, blank=True),
        ),
        migrations.AlterIndexTogether(
            name='article',
            index_together=set([]),
        ),
    ]
