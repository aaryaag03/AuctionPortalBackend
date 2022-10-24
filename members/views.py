from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users


def index(request):
    template=loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def clientLogin(request):
    template=loader.get_template('cl.html')
    return HttpResponse(template.render({},request))

def clientRegister(request):
    template=loader.get_template('cr.html')
    return HttpResponse(template.render({},request))

def clientRegistered(request):
    client_username=request.POST['username']
    client_password=request.POST['password']
    client_email=request.POST['email']

    for x in Users.objects.all().values():
        if(x['username']==client_username):
            return HttpResponse("Username taken")

    user=Users(username=client_username, role='0',password=client_password,balance=0,email=client_email)
    user.save()
    return HttpResponseRedirect(reverse('clientLogin'))

def adminLogin(request):
    template=loader.get_template('al.html')
    return HttpResponse(template.render())

def adminRegister(request):
    template=loader.get_template('ar.html')
    return HttpResponse(template.render())

def clientLoggedIn(request):
    template=loader.get_template('chome.html')
    return HttpResponse(template.render())

def adminLoggedIn(request):
    template=loader.get_template('ahome.html')
    return HttpResponse(template.render())