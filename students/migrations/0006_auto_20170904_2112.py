# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456'),
        ),
    ]