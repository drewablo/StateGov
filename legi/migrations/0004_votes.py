# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legi', '0003_auto_20140521_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('legislator', models.CharField(max_length=60)),
                ('legislation', models.CharField(max_length=8)),
                ('vote', models.CharField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
