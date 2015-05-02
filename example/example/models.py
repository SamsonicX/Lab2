__author__ = 'SamsonicX'
from django.db import models


class Teacher(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    gender = models.CharField(max_length=7)
    birth_date = models.DateField
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField()
    address = models.TextField()


class Class(models.Model):
    number = models.CharField(max_length=2)
    letter = models.CharField(max_length=1)
    year = models.IntegerField()


class Subject(models.Model):
    title = models.CharField(max_length=30)


class Table(models.Model):
    code_teacher = models.ForeignKey(Teacher)
    code_subject = models.ForeignKey(Subject)
    code_class = models.ForeignKey(Class)
    time = models.TimeField()
    day = models.CharField(max_length=3)
