from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from django.http import HttpResponse
from .models import person
# Create your views here.

def home(request):
    obj=person.objects.all()
    return render(request,'home.html',{'obj':obj})



def user_register(request):
    if request.user.is_authenticated:
    # if 'username' in request.session:
        return redirect(index)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('user_register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('user_login')
        else:
            messages.info(request,'Password does not match')
            return redirect('user_register')
    
    return render(request,'user_register.html')

def user_login(request):
    if request.user.is_authenticated:
    # if 'username' in request.session:
        return redirect(index)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # request.session['username']=username
            # auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'You are not registered')
            return redirect('user_login')
        
    
    return render(request,'user_login.html')


def index(request):
    if request.user.is_authenticated:
    # if 'username' in request.session:
    #     return render(request,'index.html')
    # return redirect(user_login)

        if request.method=='POST':
            name=request.POST.get('username','')
            dob=request.POST.get('dob','')
            age=request.POST.get('age','')
            gender=request.POST.get('gender','')
            phone=request.POST.get('phone','')
            email=request.POST.get('email','')
            address=request.POST.get('address','')
            district=request.POST.get('district','')
            branch=request.POST.get('branch','')
            account_type=request.POST.get('account','')

            materials_provide=[]
            if 'cheque' in request.POST:
                materials_provide.append('Cheque')
            if 'credit' in request.POST:
                materials_provide.append('Credit')
            if 'debit' in request.POST:
                materials_provide.append('Debit')

            # if not(name and dob and age and gender and phone and email and address and district and branch and account_type):
            #     messages.info(request,"form submitted successfully")
            #     return redirect('index')
            #     # return redirect('home')
            # return HttpResponse('Form submitted successfully')
            with open('form_data.txt','a') as file:
                file.write(f"Username: {name}, DOB: {dob}, Age: {age}, Gender: {gender}, "
                       f"Phone: {phone}, Email: {email}, Address: {address}, "
                       f"District: {district}, Branch: {branch}, Account Type: {account_type}, "
                       f"Materials Provide: {', '.join(materials_provide)}\n")
            return redirect(new_page)

        return render(request,'index.html')
    return redirect(user_login)

def new_page(request):
    if request.user.is_authenticated:
        return render(request,'new_page.html')
    return redirect(index)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    # if 'username' in request.session:
        # request.session.flush()
    # auth.logout(request)
    return redirect('home')