from json import load
from os.path import join

from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from shop.settings import BASE_DIR

from .models import Contact, Product, ProductCategory

"""
Исправил как в замечании, но мне кажеться, что предыдущий вариает был лучше.
Т.к. на сервере, если одновременно придет пара запросов, может возникнуть 
  блокировка файла, что приведет к тому, что один из потоков, будет дожидаться
  освобождение ресурса. В малых масштабах - это не сильно сыграет роли, но 
  при большом кол-ве запросов, это скажеться значительно.

Можно меню запихнуть в базу данных, однако, каждый раз тягать из базы то, что
используется постояно - увеличивает нагрузку на бд. 

Механизм запоминания - (а именно кеш) - исправит проблему, что и можно встретить,
  если завести переменную.

Будет круто, если подскажете - как реализовать загрузку меню, используя
  механизм кеша.
"""


def load_menu():
    with open(join(BASE_DIR, "shop/data/menu.json")) as m:
        return load(m)


def main(request):
    title = "главная"

    products = Product.objects.all()

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL, "menu": load_menu()}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        "menu": load_menu(),
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations, "menu": load_menu()}
    return render(request, "mainapp/contact.html", content)
