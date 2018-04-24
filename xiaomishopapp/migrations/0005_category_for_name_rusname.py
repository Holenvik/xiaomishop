# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaomishopapp', '0004_auto_20180420_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='for_name_rusname',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
