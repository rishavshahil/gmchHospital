from django.urls import path
from .views import TenderView, NoticeView
urlpatterns = [
    path('tender/', TenderView.as_view(), name='tender'),
    path('notice/', NoticeView.as_view(), name='notice'),
]