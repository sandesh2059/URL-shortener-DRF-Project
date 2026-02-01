from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def homeView(request):
    return render(request, 'home.html')

def registerView(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    
    context = {'form':form}
    return render(request, 'register.html', context)


def loginView(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('longurl-list')
        else:
            messages.info(request, 'invalid username or password')
            
    context={}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')