from django.shortcuts import render

from site_category.models import Category
from site_settings.models import Site_Setting


def header(request):
    settings = Site_Setting.objects.first()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'settings': settings,
    }

    return render(request, "shared/Header.html", context)


def home_page(request):
    settings = Site_Setting.objects.first()
    categories = Category.objects.all()
    context = {
        'title': "Home",
        'categories': categories,
        'settings': settings,
    }

    return render(request, "home_page.html", context)


def about_page(request):
    settings = Site_Setting.objects.first()
    context = {
        'title': "About-us",
        'settings': settings,
    }

    return render(request, "about_page.html", context)


def footer(request):
    settings = Site_Setting.objects.first()
    context = {
        'settings': settings,
    }

    return render(request, "shared/Footer.html", context)
