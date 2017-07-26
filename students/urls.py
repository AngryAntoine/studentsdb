from django.conf.urls import url
from .views import (students_list,
                    students_add,
                    students_edit,
                    students_delete,
                    groups_list,
                    groups_add,
                    groups_edit,
                    groups_delete,
                    )

urlpatterns = [
    url(r'^$', students_list, name='students_list'),
    url(r'^students/add/$', students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students_delete, name='students_delete'),
    url(r'^groups/$', groups_list, name='groups_list'),
    url(r'^groups/add/$', groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups_delete, name='groups_delete'),
]
