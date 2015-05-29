# -*- coding: utf-8 -*-
from models import Teacher, Class, Subject, Table
from django.contrib import admin
from django.views.generic.base import TemplateView, View
from django.shortcuts import redirect


class Teacher_Add(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        surname_value = self.request.POST['surname']
        name_value = self.request.POST['name']
        patronymic_value = self.request.POST['patronymic']
        gender_value = self.request.POST['gender']
        birth_date_value = self.request.POST['birth_date']
        phone_number_value = self.request.POST['phone_number']
        address_value = self.request.POST['address']
        Teacher.objects.create(surname=surname_value, name=name_value, patronymic=patronymic_value, gender=gender_value,
                               birth_date=birth_date_value, phone_number=phone_number_value,
                               address=address_value)
        return redirect('/')


class Teacher_Delete(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        teacher_delete = self.request.POST['teacher_delete']
        Teacher.objects.filter(id=int(teacher_delete)).delete()
        return redirect('/')


class Class_Add(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        number_value = self.request.POST['number']
        letter_value = self.request.POST['letter']
        year_value = self.request.POST['year']
        Class.objects.create(number=number_value, letter=letter_value, year=year_value)
        return redirect('/')


class Class_Delete(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        class_delete = self.request.POST['class_delete']
        Class.objects.filter(id=int(class_delete)).delete()
        return redirect('/')


class Subject_Add(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        title_value = self.request.POST['title']
        Subject.objects.create(title=title_value)
        return redirect('/')


class Subject_Delete(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        subject_delete = self.request.POST['subject_delete']
        Subject.objects.filter(id=int(subject_delete)).delete()
        return redirect('/')


class TableRecord_Add(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        teacher_value = self.request.POST['teacher']
        subject_value = self.request.POST['subject']
        class_value = self.request.POST['class']
        time_value = self.request.POST['time']
        day_value = self.request.POST['day']
        Table.objects.create(
            code_teacher=Teacher.objects.filter(id=int(teacher_value))[0],
            code_subject=Subject.objects.filter(id=int(subject_value))[0],
            code_class=Class.objects.filter(id=int(class_value))[0],
            time=time_value,
            day=day_value
        )
        return redirect('/')


class TableRecord_Delete(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        tablerecord_delete = self.request.POST['record_delete']
        Table.objects.filter(id=int(tablerecord_delete)).delete()
        return redirect('/')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        teacher_list = Teacher.objects.all()
        class_list = Class.objects.all()
        subject_list = Subject.objects.all()
        table_list = Table.objects.all()
        context.update(
            {
                'teacher_list': teacher_list,
                'class_list': class_list,
                'subject_list': subject_list,
                'table_list': table_list,
            }
        )
        return context
