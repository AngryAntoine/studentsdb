# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False, verbose_name=u'Ім\'я')
    last_name = models.CharField(max_length=100, blank=False, verbose_name=u'Прізвище')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name=u'По-батькові', default='')
    student_group = models.ForeignKey('Group', blank=False, null=True, verbose_name=u'Група', on_delete=models.PROTECT)
    birthday = models.DateField(blank=False, null=True, verbose_name=u'Дата народження')
    photo = models.ImageField(blank=True, null=True, verbose_name=u'Фото')
    ticket = models.PositiveIntegerField(blank=False, verbose_name=u'Білет')
    notes = models.TextField(blank=True, verbose_name=u'Додаткові нотатки')

    def __unicode__(self):
        return u'%s %s' % (self.last_name, self.first_name)

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенти'


class Group(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name=u'Назва')
    leader = models.OneToOneField('Student', blank=True, null=True, verbose_name=u'Староста', on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, verbose_name=u'Додаткові нотатки')

    def __unicode__(self):
        if self.leader:
            return u'%s (%s %s)' % (self.title, self.leader.last_name, self.leader.first_name)
        else:
            return u'%s' % self.title

    class Meta:
        verbose_name = u'Група'
        verbose_name_plural = u'Групи'
        # ordering = ['title']
