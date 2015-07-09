# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import livefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_optional_fields_fixes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('live', livefield.fields.LiveField(default=True)),
                ('publish_date', models.DateTimeField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('date_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('template', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to='base.Profiel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourantEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('live', livefield.fields.LiveField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=9)),
                ('text', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('date_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('courant', models.ForeignKey(to='courant.Courant', related_name='entries')),
                ('user', models.ForeignKey(to='base.Profiel')),
            ],
            options={
                'ordering': ['order', 'pk'],
            },
        ),
    ]
