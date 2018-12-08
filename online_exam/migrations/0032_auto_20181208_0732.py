# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-08 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0031_auto_20181207_2144'),
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