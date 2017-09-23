# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from ..models import Student, Group


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
    # except InvalidPage:
    #     # if page not a number, show first page
    #     students = paginator.page(1)
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
    groups = Group.objects.all().order_by('title')
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u'Ім\'я є обов\'язковим'
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u'Прізвище є обов\'язковим'
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u'Дата народження є обов\'язковою'
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                    data['birthday'] = birthday
                except Exception:
                    errors['birthday'] = u'Введіть коректний формат дати (наприклад 1986-21-02)'

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u'Номер білета є обов\'язковим'
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u'Група є обов\'язковою'
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u'Оберіть коректну групу для студента'
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            if not errors:
                student = Student(**data)
                student.save()
                return HttpResponseRedirect(
                    u'%s?status_message=Студента %s успішно додано!' % (reverse('students:students_list'),
                                                                        data['last_name'])
                )
            else:
                context = {'groups': groups,
                           'errors': errors}
                return render(request, 'students/student_add_form.html', context)
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                u'%s?status_message=Додавання студента скасовано!' % reverse('students:students_list')
            )
    else:
        context = {
            'groups': groups,
        }
        return render(request, 'students/student_add_form.html', context)


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


def contact_admin(request):
    return render(request, 'students/contact_admin.html', {})