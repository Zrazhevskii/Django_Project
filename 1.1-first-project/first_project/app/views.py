from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context=context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # разобрал несколько вариантов
    # первый с использованием templates
    # второй (внизу) вывод списком
    example_dir = '/Users/Admin/PycharmProjects/Django_Project'
    content = os.listdir(example_dir)
    return render(request, 'app/all_files_of_directory.html', context={'content': content})

# def workdir_view(request):
#     # по аналогии с `time_view`, напишите код,
#     # который возвращает список файлов в рабочей директории
#     example_dir = '/Users/Admin/PycharmProjects/Django_Project'
#     all_files = f'Рабочая директория содержит файлы: {os.listdir(example_dir)}'
#     return HttpResponse(all_files)
