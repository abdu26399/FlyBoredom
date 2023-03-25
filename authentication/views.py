from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


# Create your views here


def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']

        # Check if passwords match
        if pwd1 != pwd2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Create a user object
        try:
            myuser = User.objects.create_user(username, email, pwd1)
            myuser.first_name = firstname
            myuser.last_name = lastname

            # save in database
            myuser.save()
            messages.success(request, "Your account is successfully created.")
            return redirect('signin')

        except IntegrityError:
            messages.error(request, "This username already exists. Please try another one.")
            return redirect('signup')

    return render(request, "authentication/signup.html")


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pwd1 = request.POST['pwd1']

        user = authenticate(username=username, password=pwd1)

        #if user typed right credentials which is saved in database then login user, returns None response if user is not authenticated
        if user is not None:
            login(request,user)
            firstname = user.first_name
            return render(request, "authentication/index.html", {'firstname': firstname})

        #credentials not matched
        else:
            messages.error(request, "Incorrect credentials!")
            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"You have logged out")
    return redirect('home')
