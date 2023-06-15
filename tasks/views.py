from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

#from django.http import HttpResponse#


def home(request):
    return render(request, 'home.html'), {}

def signup(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm
            }
        return render(request, 'signup.html', context)
#cuidar los espacios, deben coincidir las funciones#
    else:
        if request.POST['password1'] == request.POST['password2']:
            #create user#
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm, 
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm, 
            'error': 'Password does not match'
        })    
    
def tasks(request):
    return render(request, 'tasks.html'), {}





#1def helloworld(request):
    #return render(request, 'signup.html'), {
        #'form': UserCreationForm(),}

#2if request.method == 'GET':
#   print('sending form')
#       else:
        #print(request.POST)
        #print('getting data')

    #return render(request, 'signup.html'), {
        #'form': UserCreationForm(),}:

#3user = User.objects.get(username=request.POST['username'])
#     return HttpResponse('Username already exists')
#         print('user created')
#       print(request.POST)
#       print('getting data')
