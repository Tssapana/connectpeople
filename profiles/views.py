from django.shortcuts import render,redirect
from .forms import LoginForm,SignupForm, UserUpdateForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='/profiles/login')
def update_profile(request):
    profile=Profile.objects.get(user=request.user)
    forms= UserUpdateForm(instance=profile)
    if request.method=='POST':
        form=UserUpdateForm(request.POST,request.FILES, instance=profile)
        # print(form.is_valid())
        if form.is_valid():
            instance=form.save(commit=False)  
            instance.user=request.user    
            instance.save()
            return redirect ("/")
    context={"form":forms}
    return render(request, "profiles/update_profile.html", context)

@login_required(login_url='/profiles/login')
def get_profile(request):
    profile=Profile.objects.get(user=request.user)
    context={"profile":profile}
    return render(request,"profiles/profile.html",context)




