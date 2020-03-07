from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing Error Message')
        return redirect('register')
    else:
        return render (request, 'account/register.html')

def login(request):
    if request.method == 'POST':
        #login
        return
    else:
        return render (request, 'account/login.html')

def logout(request):
    return redirect ('index')

def dashboard(request):
    return render (request, 'account/dashboard.html')