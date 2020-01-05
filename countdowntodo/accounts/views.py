from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def signup(request):
    return render(request, 'signup.html')


class HomePageView(TemplateView):
    template_name = 'home.html'
