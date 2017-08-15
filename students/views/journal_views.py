# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Views for Students.
def journal(request):
    context = {}
    return render(request, 'students/journal.html', context)
