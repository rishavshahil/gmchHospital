from django.shortcuts import render
from django.views import View
from .models import HospitalNotice, HospitalTender

class TenderView(View):
    template_name = 'notification/tender.html'

    def get(self, request, *args, **kwargs):
        tenders = HospitalTender.objects.all()
        return render(request, self.template_name, {'tenders': tenders})
    

class NoticeView(View):
    template_name = 'notification/notice.html'

    def get(self, request, *args, **kwargs):
        notices = HospitalNotice.objects.all()
        return render(request, self.template_name, {'notices': notices})