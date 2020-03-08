from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "This Username is taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email
                    , first_name=first_name, last_name=last_name)
                    #login after register
                    # auth.login(request, user)
                    # messages.success(request, "You are logged in!")
                    # return redirect('/')
                    user.save()
                    messages.success(request, "Registration Successful!")
                    return redirect ('login')
        else:       
            messages.error(request, 'Passwords do not match!')
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