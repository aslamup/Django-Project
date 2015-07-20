from django.shortcuts import render
from django.shortcuts import render,redirect
from models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import random

# Create your views here.
def register(request):
    if request.method == 'POST':
        try:
            user_exists = User.objects.get(username=request.POST['username'])
            return HttpResponse("Username already exists!")
        except User.DoesNotExist:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()
            data={'i':[1,2,3]}
    
    return render(request,"home.html",data)

@login_required
def home(request):
    return render(request,"welcome.html",{'name':request.user.username})

def loginapp(request):
    ''' for signup or login '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
        else:
            return render(request, "home.html", {"error": 'error'})

    return render(request, "home.html", {})
    


def logoutapp(request):
    logout(request)
    return HttpResponseRedirect("/login/")


def add_details(request):
    if request.method =='POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')

        p= Person()
        p.user = request.user
        p.name = name
        p.address = address
        p.city = city
        p.mobile = mobile
        p.save()
        i=0
        while(i<3):
            deg='deg[%s]' % i
            per='per[%s]' % i
            col='col[%s]' % i

            degree=request.POST.get(deg)
            percentage=request.POST.get(per)
            college=request.POST.get(col)

            e= Education()
            e.e_id=request.user
            e.degree=degree
            e.percentage=percentage
            e.college=college
            e.save()
            i=i+1

    return render(request,"success.html")

def  add_question(request):

    d=[1,2]
    rd=random.choice(d)
    name=Question.objects.values('name').get(id=rd)
    address=Question.objects.values('address').get(id=rd)
    city=Question.objects.values('city').get(id=rd)
    mobile=Question.objects.values('mobile').get(id=rd)
    #degree=Question.objects.values('degree').get(id=rd)
    #percentage=Question.objects.values('percentage').get(id=rd)
    #college=Question.objects.values('college').get(id=rd)
    val ={'name':name['name'],'address':address['address'],'city':city['city'],'mobile':mobile['mobile']}
    return render(request,"main.html",val)

def  view_profile(request):
    CurrentUser=Person.objects.values('name','address','city','mobile').get(user_id=request.user.id)
    data={'CurrentUser':CurrentUser['name'],'address':CurrentUser['address'],'city':CurrentUser['city'],'mobile':CurrentUser['mobile']}
    Edn_details=Education.objects.filter(e_id=request.user.id).all()
    data.update({'edu': Edn_details})
    return render(request,"profile.html",data)
