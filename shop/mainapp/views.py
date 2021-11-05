from json import load
from os.path import join

from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from shop.settings import BASE_DIR

from .models import Product, ProductCategory, Contact

with open(join(BASE_DIR, "shop/data/menu.json")) as m:
    menu = load(m)

def main(request):
    title = "главная"

    products = Product.objects.all()

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL, "menu": menu}
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
        "menu": menu,
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations, "menu": menu}
    return render(request, "mainapp/contact.html", content)
