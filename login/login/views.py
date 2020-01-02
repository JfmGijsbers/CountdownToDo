from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.urls import reverse


#@login_required
#def home(request):
#    return HttpResponseRedirect(
#        '',
#                args=[request.user.username]
#    )


def lgdin(request):
    return render(request, )


#@login_required(login_url='/')
#def home(request):
 #   return HttpResponseRedirect(
 #       reverse(lgdin(request),
 #               args=[request.user.username])
 #   )
def home(request):
    return render(request, 'dashboard/home.html')


