from django.conf.urls import url
from views.students_views import (students_list,
                                  students_add,
                                  students_edit,
                                  students_delete,
                                  )
from views.groups_views import (groups_list,
                                groups_add,
                                groups_edit,
                                groups_delete,
                                )
from views.journal_views import (journal)

urlpatterns = [
    url(r'^$', students_list, name='students_list'),
    url(r'^students/add/$', students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students_delete, name='students_delete'),
    url(r'^journal/$', journal, name='journal'),
    url(r'^groups/$', groups_list, name='groups_list'),
    url(r'^groups/add/$', groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups_delete, name='groups_delete'),
]
