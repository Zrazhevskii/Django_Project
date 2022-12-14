from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    # context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    students = Student.objects.prefetch_related('teachers')
    print(students[0].teachers.all())
    result = students.order_by(ordering)
    context = {'object_list': result}

    return render(request, template, context)
