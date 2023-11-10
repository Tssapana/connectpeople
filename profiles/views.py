from django.shortcuts import render,redirect
from .forms import LoginForm,SignupForm
from django.contrib.auth import authenticate, login

# Create your views here.

def user_login(request):
    forms=LoginForm()
    if  request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
    context={"form":forms}
    return render(request, 'profiles/login.html', context)

def signup(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/profiles/login")
        
    context={"form":form}
    return render(request, "profiles/signup.html", context)

