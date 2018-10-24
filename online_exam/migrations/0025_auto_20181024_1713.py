# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-24 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0024_auto_20181024_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_detail',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_exam.course'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_exam.user'),
        ),
    ]
