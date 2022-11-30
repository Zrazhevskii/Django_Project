from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    templates = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort', '')

    if sort == 'name':
        phones_str = phones.order_by('name')
    elif sort == 'max_price':
        phones_str = phones.order_by('max_price')
    elif sort == 'mix_price':
        phones_str = phones.order_by('mix_price').reverse()
    else:
        phones
    context = {'phones': phones_str}
    return render(request, templates, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
