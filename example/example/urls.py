from django.conf.urls import patterns, url

from django.contrib import admin

from views import IndexView, Teacher_Add, Teacher_Delete, Class_Add, Class_Delete, Subject_Add, Subject_Delete, \
    TableRecord_Add, TableRecord_Delete

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^teacher_add', Teacher_Add.as_view()),
    url(r'^teacher_delete', Teacher_Delete.as_view()),
    url(r'^class_add', Class_Add.as_view()),
    url(r'^class_delete', Class_Delete.as_view()),
    url(r'^subject_add', Subject_Add.as_view()),
    url(r'^subject_delete', Subject_Delete.as_view()),
    url(r'^record_add', TableRecord_Add.as_view()),
    url(r'^record_delete', TableRecord_Delete.as_view()),
    url(r'^$', IndexView.as_view())
)
