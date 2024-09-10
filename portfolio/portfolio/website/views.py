from django.shortcuts import render

def signUpPage(request):
    return render(request, 'registration.html')

def loginPage(request):
    return render(request, 'login.html')

def homePage(request):
    return render(request, 'home.html')
