from django.shortcuts import render
from django.http import HttpResponse
from .forms import regerstrationInput
# Create your views here.
def home(request):
    context={}
    return render(request,"home.html",context)
def register(request):
    context ={}
    context['form']= regerstrationInput()
    return render(request, "registration.html",context)
def submit(request):
    context={}
    return render(request,"show.html",context)