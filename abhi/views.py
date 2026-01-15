from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required(login_url="/login")
def index(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        u=User.objects.filter(username=username)
        if u:
            messages.error(request,"username exists")
            return redirect("signup")
        else:
            user=User.objects.create(username=username, email=email, first_name=firstname,last_name=lastname)
            user.set_password(password)
            user.save()
            return redirect("login")
    return render(request, "signup.html")

def loginp(request):
    if request.method=="POST":
        use=request.POST.get("use")
        pas=request.POST.get("pass")
       
        hi=User.objects.filter(username=use).exists()
        
        if hi:
            bye=authenticate(username=use,password=pas)
            if bye:
                login(request,bye)
                return redirect("index")
            else:
                messages.error(request,"wrong password")
                print("hi")
                return redirect("login")
            
    return render(request, "login.html")

@login_required(login_url="/login")
def logoutp(request):
    logout(request)
    return redirect("login")

@login_required(login_url="/login")
def write(request):
    if request.method=="POST":
        date=request.POST.get("date")
        write=request.POST.get("area")
        hi=request.user
        para.objects.create(user=hi,date=date,write=write)
        return redirect("index")
    return render(request, "write.html")

@login_required(login_url="/login")
def read(request):
    if request.method=="POST":
        d=request.POST.get("date")
        hlo=request.user
        p=para.objects.filter(user=hlo,date=d)
        print(p)
        return render(request, "read.html",{'p':p})
    else:
        bye=request.user
        p=para.objects.filter(user=bye)
        return render(request, "read.html",{'p':p})

def base(request):
    return render(request,"base.html")