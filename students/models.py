# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False, verbose_name=u'Ім\'я')
    last_name = models.CharField(max_length=100, blank=False, verbose_name=u'Прізвище')
    middle_name = models.CharField(max_length=100, blank=False, verbose_name=u'По-батькові', default='')
    birthday = models.DateField(blank=False, null=True, verbose_name=u'Дата народження')
    photo = models.ImageField(blank=True, null=True, verbose_name=u'Фото')
    ticket = models.CharField(max_length=100, blank=False, verbose_name=u'Білет')
    notes = models.TextField(blank=True, verbose_name=u'Додаткові нотатки')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенти'