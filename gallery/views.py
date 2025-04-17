from django.shortcuts import render
from django.views import View
from .models import Gallery, GalleryImage

class GalleryView(View):
    template_name = 'gallery/gallery.html'

    def get(self, request, *args, **kwargs):
        galleries = Gallery.objects.all()

        return render(request, self.template_name, {'galleries': galleries})
    

class GalleryImageView(View):
    template_name = 'gallery/gallery-img.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)