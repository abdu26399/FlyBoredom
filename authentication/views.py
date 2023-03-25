from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here

def home(request):
    # Render the index.html template
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        # Get the form data
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']

        # Create a user object
        try:
            myuser = User.objects.create_user(username, email, pwd1)
            myuser.first_name = firstname
            myuser.last_name = lastname

            # Save the user object to the database
            myuser.save()

            # Add a success message and redirect to the signin page
            messages.success(request, "Your account is successfully created.")
            return redirect('signin')

        except IntegrityError:
            return redirect('signin')

    # Render the signup.html template
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        # Get the form data
        username = request.POST['username']
        pwd1 = request.POST['pwd1']

        # Authenticate the user using the entered credentials
        user = authenticate(username=username, password=pwd1)

        # If the user is authenticated, log them in and redirect to the index page with their name displayed
        if user is not None:
            login(request,user)
            firstname = user.first_name
            return render(request, "authentication/index.html", {'firstname': firstname})

        # If the user is not authenticated, add an error message and redirect back to the home page
        else:
            messages.error(request, " Incorrect credentials! Please check your Username and Password. Try again")
            return redirect('home')

    # Render the signin.html template
    return render(request, "authentication/signin.html")


def signout(request):
    # Log out the user and add a success message
    logout(request)
    messages.success(request,"You have logged out")

    # Redirect to the home page
    return redirect('home')
