# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponse
from django.shortcuts import render


# Views for Students.
def students_list(request):
    students = (
        {'id': 1,
         'first_name': 'Антон',
         'last_name': 'Граменко',
         'ticket': 21,
         'image': 'img/Anton.jpg'},
        {'id': 2,
         'first_name': 'Дмитро',
         'last_name': 'Граменко',
         'ticket': 12,
         'image': 'img/Dima.jpg'},
        {'id': 3,
         'first_name': 'Наташа',
         'last_name': 'Холодняк',
         'ticket': 212,
         'image': 'img/Natasha.jpg'},
    )
    context = {
        'students': students,
    }
    return render(request, 'students/students_list.html', context)


def students_add(request):
    title = 'Hello, student add'
    context = {
        'title': title,
    }
    return render(request, 'base.html', context)


def students_edit(request, sid):
    title = 'Hello, student %s edit' % sid
    context = {
        'title': title,
    }
    return render(request, 'base.html', context)


def students_delete(request, sid):
    title = 'Hello, student %s delete' % sid
    context = {
        'title': title,
    }
    return render(request, 'base.html', context)


# Views for Groups.
def groups_list(request):
    title = 'Hello, group'
    context = {
        'title': title,
    }
    return render(request, 'students/groups_list.html', context)


def groups_add(request):
    title = 'Hello, group add'
    context = {
        'title': title,
    }
    return render(request, 'base.html', context)


def groups_edit(request, gid):
    title = 'Hello, group %s edit' % gid
    context = {
        'title': title,
    }
    return render(request, 'base.html', context)


def groups_delete(request, gid):
    title = 'Hello, group %s delete' % gid
    context = {
        'title': title,
    }
    return render(request, 'base.html', context)
