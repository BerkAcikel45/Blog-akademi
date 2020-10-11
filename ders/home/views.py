from django.shortcuts import render
from django.views.generic import TemplateView


#function based view
def about(request):
    template = 'about.html'
    return render(request, template, {})


#class based view
class homeView(TemplateView):
    template_name = 'main.html'
