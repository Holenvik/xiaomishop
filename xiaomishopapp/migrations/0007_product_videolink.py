# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaomishopapp', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='videolink',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
