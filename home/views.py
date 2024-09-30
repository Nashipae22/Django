from django.shortcuts import render
from django.http import HttpResponse
from. models import Products, Category

# Create your views here.
def home(request):
 products=Products.objects.all()
 return render(request, "home/homep.html", {'products': products})

def house(request):
 household_category=Category.objects.get(name="Household Items")
 products=Products.objects.filter(category=household_category)
 return render(request, "home/homep.html", {'products': products})

def elect(request):
 household_category=Category.objects.get(name="Electronic Items")
 products=Products.objects.filter(category=household_category)
 return render(request, "home/homep.html", {'products': products})


def bath(request):
 household_category=Category.objects.get(name="Bathroom Items")
 products=Products.objects.filter(category=household_category)
 return render(request, "home/homep.html", {'products': products})


def kitch(request):
 household_category=Category.objects.get(name="Kitchen items")
 products=Products.objects.filter(category=household_category)
 return render(request, "home/homep.html", {'products': products})

def search(request):
 products= Products.objects.order_by('name')
 return render(request, 'home/homep.html',{'products':products})

def more(request):
 return HttpResponse('Moree')
