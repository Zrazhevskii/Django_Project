import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones1.csv', encoding='utf-8') as file:
            phons = csv.DictReader(file, delimiter=';')

            for phone in phons:
                Phone.objects.create(
                    id=phone['id'],
                    name=phone['name'],
                    image=phone['image'],
                    price=int(phone['price']),
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug=slugify(phone['name'])
                )
