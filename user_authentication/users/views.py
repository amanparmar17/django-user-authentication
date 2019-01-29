from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm


def index(request):
	return render(request,'users/index.html')

def register(request):
	form=UserCreationForm()
	return render(request,'registration/register.html',{'form':form})