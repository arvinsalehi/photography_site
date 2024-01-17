from django.shortcuts import render


def services_page(request):
    context = {

    }
    return render(request, 'services-page.html', context)
