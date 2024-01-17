from django.urls import path

from site_contact.views import contact_page

app_name = 'Contact_Us'

urlpatterns = [
    path('contact-us', contact_page, name='contact')
]