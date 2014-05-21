# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_action', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legislation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_action_date', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legislator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='bill',
            field=models.ForeignKey(to='legi.Legislation', to_field='id'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='last_action',
            field=models.ForeignKey(to='legi.Action', to_field='id'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='name',
            field=models.ForeignKey(to='legi.Legislator', to_field='id'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='last_action_date',
            field=models.ForeignKey(to='legi.Date', to_field='id'),
        ),
    ]
