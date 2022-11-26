from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


# def bus_stations(request):
# получите текущую страницу и передайте ее в контекст
# также передайте в контекст список станций на странице

# context = {
#     'bus_stations': ...,
#     'page': ...,
# }
# return render(request, 'stations/index.html', context)

def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        data_list = []
        data = csv.DictReader(file)
        for line in data:
            data_dict = {'Name': line['Name'], 'Street': line['Street'], 'District': line['District']}
            data_list.append(data_dict)
        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(data_list, 10)
        page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
