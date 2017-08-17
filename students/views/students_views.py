# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..models import Student
# from django.http import HttpResponse
from django.shortcuts import render


# Views for Students.
def students_list(request):
    students = Student.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('first_name', 'last_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

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
