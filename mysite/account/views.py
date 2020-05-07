from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Create_user_form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticate_user,allowed_user,admin_only
from django.contrib.auth.models import Group
# Create your views here.


@login_required(login_url='account:loginpage')
@admin_only
def index(request):
    return render(request,'account/index.html')

@login_required(login_url='account:loginpage')
@allowed_user(allowed_roles=['vist'])
def userpage(request):
    context = {}
    return render(request,'account/user.html',context)


@unauthenticate_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('usernmae')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index') 
        else:
            messages.info(request,'Username or password is incorrect')
            return render(request,'account/loginpage.html')

    return render(request,'account/loginpage.html')

@unauthenticate_user
def registation(request):
    form = Create_user_form()

    if request.method == 'POST':
        form = Create_user_form(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='vist')
            user.groups.add(group)
            messages.success(request,"account was created for "+ username)
            return redirect('account:loginpage')

    context = {'form':form}
    return render(request,'account/register.html',context)


def logoutuser(request):
    logout(request)
    return redirect('account:loginpage')

@login_required(login_url='account:loginpage')
@allowed_user(allowed_roles=['vist'])
def profile(request):
    print(request.user.cust.profile_pic.url)
    context= {}
    return render(request,'account/profile.html',context)