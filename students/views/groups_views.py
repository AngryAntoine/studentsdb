# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponse
from django.shortcuts import render


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
