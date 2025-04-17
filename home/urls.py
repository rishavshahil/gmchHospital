from django.urls import path
from .views import HomeView, AboutView, OPDView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about-us/', AboutView.as_view(), name='about'),
    path('opd-schedule/', OPDView.as_view(), name='opd'),
]