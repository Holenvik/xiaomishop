# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xiaomishopapp', '0002_auto_20180414_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=100)),
                ('phone', models.CharField(verbose_name='Номер телефона', max_length=100)),
                ('address', models.CharField(verbose_name='Адрес', max_length=100)),
                ('user', models.OneToOneField(related_name='xiaomishop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары', 'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
