from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import logout
from django.shortcuts import redirect
from . forms import CreateUserForm

def homepage(request):

    return render(request, 'base/index.html')

def register(request):

    # form = CreateUserForm()

    if request.method == "POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1!=password2:
            return HttpResponse("Your password didn't match!!!")
        else:
            my_user=User.objects.create_user(uname,email,password1)
            my_user.save()
            return redirect('user-login')
        print(uname,email,password1,password2)

        # form = CreateUserForm(request.POST)

    #     if form.is_valid():

    #         form.save()

    #         return redirect("user-login")
        
    # context = {'registerform':form}


    return render(request, 'base/auth/register.html')







def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse('Username or Password is incorrect!')


    return render(request, 'base/auth/login.html')


def dashboard(request):

    return render(request, 'base/home/myhome.html')

def user_logout(request):
    logout(request)
    return redirect("user-login")





