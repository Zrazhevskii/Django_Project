from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    templates = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')

    if sort == 'name':
        phones_str = phones.order_by('name')
    elif sort == 'max_price':
        phones_str = phones.order_by('-price')
    elif sort == 'min_price':
        phones_str = phones.order_by('price')
    else:
        phones_str = phones
    context = {'phones': phones_str}
    return render(request, templates, context)


def show_product(request, slug):
    templates = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, templates, context)
