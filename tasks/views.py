from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html'), {}

def signup(request):

   if request.method == 'GET':
        return render(request, 'signup.html'), {
        'form': UserCreationForm(),})
        print('sending form')
    else:
        if request.POST['password1'] == request.POST['password1']:
            #create user#
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HTTPResponse('User created successfully')
            except: 
                return HttpResponse('Username already exists')
        return HttpResponse('Password does not match')




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
