from django.urls import path
from .views import HomePageView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/', HomePageView.as_view(), name='home')
]