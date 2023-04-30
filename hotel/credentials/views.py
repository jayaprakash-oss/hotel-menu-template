from django.shortcuts import render,redirect
# from credentials.models import register as r
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def register(request):
    if request.method=="POST":
        fname=request.POST["Fname"]
        uname=request.POST["User"]
        lname=request.POST["Lname"]
        # mobile=request.POST["Mobile"]
        email=request.POST["Email"]
        # country=request.POST["Country"]
        password=request.POST["Password"]
        # re_password=request.POST["re"]
        

        if fname=='' or lname=='' or email=='' or password=='' or uname=='':
            # messages.info(request,"Required Field")
            return redirect('register.html')
                
        else:
            if password==password:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
                user.save()
                return redirect('/')
            # messages.info(request,"User Registered Successfully!")
            
            # messages.info(request,"")
            # print("One record Inserted!")
    else:
        return render(request,"register.html")



def login(request):
   
    if request.method=="POST": 
        password=request.POST["password"]
        username=request.POST["username"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"No such User")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })