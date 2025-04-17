from django.shortcuts import render
from django.views import View
from department.models import OPD_Schedule


class HomeView(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class AboutView(View):
    template_name = 'home/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class OPDView(View):
    template_name = 'home/opd.html'

    def get(self, request, *args, **kwargs):
        opd_schedules = OPD_Schedule.objects.all()
        return render(request, self.template_name, {"opd_schedules":opd_schedules})