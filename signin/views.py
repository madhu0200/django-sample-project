from django.http import HttpResponse
from django.shortcuts import render
from numpy import unicode_
from django.db import connection
from django.shortcuts import get_object_or_404,HttpResponseRedirect
from usersignin.models import register,signuser
from .forms import GeeksForm
#rom usersignin.modeltofetch import *


def home(request):
    context={}
    return render(request,'home.html',context)


def registration(request):
    context={}
    return render(request,'registration.html',context)


def registeruser(request):
    n="hiii"
    #to get the data which is entered in the form
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        email=request.POST.get("email")
        password = request.POST.get("password")
        mobileno=int(request.POST.get("mobileno"))
        #to transer the data in the form of positional arguments to the model of register
        data=register(fname=fname,lname=lname,email=email,mobileno=mobileno,password=password)
        #saving the data in the table
        data.save()
        n="registered successfully "+email
        #to give the respose to the user
    return HttpResponse(n)
    #return render(request,'registration.html',{'n':n})


def signinuser(request):
    context={}
    #to show the signin page to the user
    return render(request,'signin.html',context)


def signin(request):
    #
    password=request.POST.get("password")
    email=request.POST.get("email")
    data=signuser.objects.all();
    #return HttpResponse(request,data)
    return render(request,'show.html',{'fetchdata':data})



def update(request):
    context={}
    #to redirect
    return render(request,'update.html',context)


def updateUser(request):
    context = {}
    #if request.method == "POST":
    fname = request.POST.get("firstname")
    lname = request.POST.get("lastname")
    mail = request.POST.get("email")
    password = request.POST.get("password")
    mobileno = int(request.POST.get("mobileno"))
    context={ }
    object=signuser.objects.filter(email=mail).delete()
    data = register(fname=fname, lname=lname, email=mail, mobileno=mobileno, password=password)
    data.save()
    return render(request,'show.html',{'fetchdata':context})


def deleteView(request):
    context={}
    return render(request,'delete.html',context)


def deleteViewUser(request):
    if request.method=="POST":
        mail=request.POST.get("email")
        #return HttpResponse(mail)
    context={}
    object=register.objects.filter(email=mail).delete()
    return HttpResponse(request,"deleted user : "+mail)

def show(request):

    return render(request,'showuser.html')

def showuser(request):
    if request.method=="POST":
        mail=request.POST.get("email")
    object=register.objects.filter(email=mail)
    context={}
    context['fetchdata']=object
    return render(request,'show.html',context)