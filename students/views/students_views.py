# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from ..models import Student


# Views for Students.
def students_list(request):
    students = Student.objects.all().order_by('last_name')
    order_by = request.GET.get('order_by', 'last_name')
    # if order_by in ('last_name',):
    #     students = Student.objects.order_by('last_name')
    if order_by in ('first_name', 'last_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    paginator = Paginator(students, 4)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # if page not a number, show first page
        students = paginator.page(1)
    except EmptyPage:
        #  if page out of range, show last page
        students = paginator.page(paginator.num_pages)

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
