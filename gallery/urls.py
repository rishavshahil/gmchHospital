from django.urls import path
from .views import GalleryView, GalleryImageView
urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),
    path('<slug:slug>/', GalleryImageView.as_view(), name='gallery_img'),
]