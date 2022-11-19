from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def course(request):
    # return HttpResponse("This is courses page")
    return render(request, 'course.html')

def about(request):
    return HttpResponse("This is about page")
    

def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == 'POST':
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        contact = Contact(name=name, message = msg, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message Submitted Successfully!\n THANK YOU')
    return render(request, 'contact.html')

def loginUser(request):
    # return HttpResponse("login")
    if request.method == "POST":
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(username=uname, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def singup(request):
    # return HttpResponse('singup')
    if request.method == "POST":
        uname = request.POST.get('uname')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.create_user(username = uname, password = password, email = email, first_name = fname, last_name = lname)
            user.save()
        except:
            return redirect("/singup")
        messages.success(request, "Account created")
    return render(request, 'singup.html')

# def doremon(request):
#     return render(request, 'doremon.html')