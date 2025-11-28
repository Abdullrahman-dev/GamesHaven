from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Profile
# Create your views here.

def registration(requset) :
    
    if requset.method == "POST" :
        try :
            if requset.POST["password"] != requset.POST["password2"] :
                messages.error(requset,"Passwords dosen't match !","alert-danger")
            
            new_user = User.objects.create_user(username=requset.POST["email"],password=requset.POST["password"],first_name=requset.POST["username"])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            messages.success(requset,"Registration Successfuly","alert-success")
            return redirect("Auth:loginn")

        except Exception as e:
            print(e)

    return render(requset,"Auth/registration.html")


def loginn(requset) :

    if requset.method == "POST": 
        email = requset.POST["email"]
        password = requset.POST["password"]

        user = authenticate(requset,username=email,password=password)
        
        if user :
            login(requset,user)
            messages.success(requset,"Logged in successfuly","alert-success")

            return redirect(requset.GET.get("next","/"))
        
        else :
                messages.error(requset,"Email or Passwords dosen't match !","alert-danger")

    return render(requset,"Auth/login.html")


def logoutt(requset) :
    logout(requset)
    messages.success(requset,"Logged out Successfuly","alert-success")
    return redirect(requset.GET.get("next","/"))


def profile(requset,user_id) :
    try :
        user = User.objects.get(pk=user_id)
        user_profile = user.profile
    except :
        return render(requset,'404.html')
    
    return render(requset, "Auth/profile.html", {"user_profile": user_profile})