from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from. models import Products, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def home(request):
 products=Products.objects.all()
 return render(request, "home/homep.html", {'products': products})

def user_signup(request):
 if request.user.is_authenticated:
  return redirect('home')
 else:
  form=CreateUserForm()
 if request.method=="POST":
  form=CreateUserForm(request.POST)
  if form.is_valid():
   form.save()
   user=form.cleaned_data.get('username')
   messages.success(request,'Account was created for '+user)
   return redirect('login')

 context={'form':form}
 return render(request,"home/signup.html", context)
 
def user_login(request):
 if request.user.is_authenticated:
    return redirect('home')
 else:
  if request.method=="POST":
     username= request.POST.get('username')
     password= request.POST.get('password')

     user=authenticate(request,username=username, password=password)

    
     if user is not None:
        login(request, user)
        return redirect('/homep/')
     else:
       messages.info(request, 'username or password is incorrect')
       context=()
 return render(request, "home/login.html")
  
def user_logout(request):
 logout(request)
 return redirect('/login/')
  
@login_required(login_url="login")
def house(request):
 household_category=Category.objects.get(name="Household Items")
 products=Products.objects.filter(category=household_category)
 return render(request, "home/homep.html", {'products': products})

@login_required(login_url="login")
def elect(request):
 household_category=Category.objects.get(name="Electronic Items")
 products=Products.objects.filter(category=household_category)
 return render(request, "home/homep.html", {'products': products})

@login_required(login_url="login")
def bath(request):
 household_category=Category.objects.get(name="Bathroom Items")
 products=Products.objects.filter(category=household_category)
 return render(request, "home/homep.html", {'products': products})

@login_required(login_url="login")
def kitch(request):
 household_category=Category.objects.get(name="Kitchen items")
 products=Products.objects.filter(category=household_category)
 return render(request, "home/homep.html", {'products': products})


def search(request):
 products= Products.objects.order_by('name')
 return render(request, 'home/homep.html',{'products':products})

@login_required(login_url="login")
def more(request):
 return HttpResponse('Moree')
