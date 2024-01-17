from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from site_category.models import Category
from site_photo.models import Photo


class Gallery(ListView):
    template_name = "Gallery.html"

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = Category.objects.get_queryset().filter(name__iexact=category_name).first()
        if category is None:
            raise Http404()
        category.visit += 1
        category.save()
        return Photo.objects.get_by_category(category_name)

    def get_context_data(self, *args, **kwargs):
        category_name = self.kwargs['category_name']
        context = super(Gallery, self).get_context_data(*args, **kwargs)
        context['category_name'] = category_name
        return context


def photo_visit(request, *args, **kwargs):
    photo_id = kwargs['photo_id']
    print(photo_id)
    photo: Photo = Photo.objects.get_by_id(photo_id)
    if photo is None:
        raise Http404()
    # photo.visit += 1
    photo.save()
    return render(request, 'Gallery.html', {})

