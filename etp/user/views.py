from django.shortcuts import render,redirect

def personalprofile(request):
    return render(request,"uprofile.html")

def editprofile(request):
    return render(request,"editprofile.html")

def pep(request):
    return render(request,"pep.html")

def cart(request):
    return render(request,"cart.html")



# Create your views here.