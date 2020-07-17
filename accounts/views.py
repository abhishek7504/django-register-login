from django.shortcuts import render, get_object_or_404
from . forms import UserRegistrationForm ,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login

def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      cd = user_form.cleaned_data
      
      # Create a new user object but avoid saving yet
      new_user = user_form.save(commit=False)
      # set the chosen password
      new_user.set_password(cd['password'])
      #save the user  objects
      new_user.save()

      return HttpResponse('Register Successfull')
  else:
    user_form = UserRegistrationForm()
  return render(request, "accounts/register.html", 
                                                  {'user_form':user_form})


def client_login(request):
    message = None
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse('Now are logged in')
            else:
                print(login_form.errors)
                return HttpResponse('Some error')
        else:
            print(login_form.errors)
            return HttpResponse('Some error')
    else:
        login_form = LoginForm()
        return render(request,'accounts/login.html',{'login_form':login_form,'message':message})