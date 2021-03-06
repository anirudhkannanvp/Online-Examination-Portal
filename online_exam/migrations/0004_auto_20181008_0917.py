# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-08 09:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=15)),
                ('email', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('account_type', models.IntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('modified', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor1',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor3',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor4',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor5',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor6',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor7',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor8',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sensor9',
        ),
        migrations.RemoveField(
            model_name='course',
            name='serialId',
        ),
        migrations.RemoveField(
            model_name='course',
            name='time',
        ),
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
