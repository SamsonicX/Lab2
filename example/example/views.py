# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from models import Teacher, Class, Subject, Table
from django.contrib import admin

teacher_list = Teacher.objects.all()
class_list = Class.objects.all()
subject_list = Subject.objects.all()
table_list = Table.objects.all()


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'teacher': teacher_list,
                'class': class_list,
                'subject': subject_list,
                'table': table_list,
            }
        )
        return context