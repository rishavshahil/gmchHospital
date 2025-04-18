from django.shortcuts import render
from django.views import View

class EventView(View):
    template_name = 'event/event.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)