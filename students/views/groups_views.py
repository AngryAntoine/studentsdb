# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from ..models import Group


# Views for Groups.
def groups_list(request):
    groups = Group.objects.all().order_by('title')
    order_by = request.GET.get('order_by', '')
    # select_qty = request.GET.get('select_qty', '1')
    # if order_by in ('last_name',):
    #     students = Student.objects.order_by('last_name')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # if page not a number, show first page
        groups = paginator.page(1)
    except EmptyPage:
        #  if page out of range, show last page
        groups = paginator.page(paginator.num_pages)

    context = {
        'groups': groups,
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
