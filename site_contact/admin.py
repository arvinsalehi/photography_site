from django.contrib import admin

from site_contact.models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_read']
    list_filter = ['is_read']
    search_fields = ["subject", "name"]


admin.site.register(ContactUs, ContactAdmin)
