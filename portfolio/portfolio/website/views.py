from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login

User = get_user_model()

def signUpPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        confirm_password = request.POST['passConf']
        email = request.POST['email']
        name = request.POST['name']
        age = request.POST.get('age')
        location = request.POST['location']
        bio = request.POST['bio']

        if password != confirm_password:
            return render(request, 'registration.html', {'error': "Passwords do not match."})

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            name=name,
            age=age,
            location=location,
            bio=bio
        )
        user.save()
        return redirect('login')

    return render(request, 'registration.html')

def loginPage(request):
    if request.method == 'POST':
        login_username = request.POST.get('name')
        login_pass = request.POST.get('password')
        user = authenticate(request, username = login_username, password = login_pass)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Password Incorrect!")
    return render(request, 'login.html')

def homePage(request):
    return render(request, 'home.html')
