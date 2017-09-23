# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404

from ..models import Testing


def test_list(request):
    tests = Testing.objects.all()
    context = {'tests': tests}
    return render(request, 'students/test_list.html', context)


def test_edit(request, tid):
    test = get_object_or_404(Testing, id=tid)
    context = {'test': test}
    return render(request, 'students/test_edit.html', context)
