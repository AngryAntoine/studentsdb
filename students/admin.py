# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import (Student,
                     Group,
                     Testing
                     )
from django.contrib import admin

# Register your models here.

admin.site.register(Student)

admin.site.register(Group)

admin.site.register(Testing)
