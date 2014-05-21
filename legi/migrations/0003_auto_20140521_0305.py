# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legi', '0002_auto_20140521_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamber',
            name='legislator',
            field=models.CharField(default='Name', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamber',
            name='legislation',
            field=models.CharField(default='Bill Number', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamber',
            name='actions',
            field=models.CharField(default='Last Action', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamber',
            name='dt',
            field=models.CharField(default='Last Action Date', max_length=10),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='chamber',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='chamber',
            name='last_action',
        ),
        migrations.RemoveField(
            model_name='chamber',
            name='last_action_date',
        ),
        migrations.RemoveField(
            model_name='chamber',
            name='name',
        ),
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.DeleteModel(
            name='Legislator',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Legislation',
        ),
    ]
