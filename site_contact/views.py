from django.shortcuts import render

from site_contact.forms import ContactUsFrom
from site_contact.models import ContactUs
from site_settings.models import Site_Setting


def contact_page(request):
    site_settings = Site_Setting.objects.first()
    contact_form = ContactUsFrom(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('first_name')
        last_name = contact_form.cleaned_data.get('last_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(name=name, last_name=last_name, email=email, subject=subject, text=text)
        contact_form = ContactUsFrom()

    context = {
        'contact_form': contact_form,
        'site_setting': site_settings,
    }
    return render(request, 'contact.html', context)
