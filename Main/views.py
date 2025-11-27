from django.shortcuts import render,redirect
from Games.models import Game , Category
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    
    games = Game.objects.all()[0:3]
    # FIX: Changed from a set {"games", games} to a dictionary {"games": games}
    populer_games = Game.objects.all().order_by("-rating")[0:6]
    return render(request,"Main/home.html",{"games": games,"populer_games":populer_games})

# For Dark And Light Mode :
def mode_view(request,mode):
    response = redirect(request.GET.get("next","/"))
    if mode == "light":
        response.set_cookie("mode","light")
    elif mode == "dark":
        response.set_cookie("mode","dark")
    return response
    
def contact(request):

    if not request.user.is_authenticated :
        messages.error(request,"Only Registered Users Can Add Review","alert-danger")
        return redirect("Auth:loginn")

    if request.method == "POST":
        
        contact = Contact.objects.create(
            subject = request.POST["subject"],
            message = request.POST["message"],
            user = request.user,
        )

        contact.save()
        messages.success(request,"Your Message Sended Successfuly","alert-success")
        return redirect("Main:contact")
    
    return render(request,"Main/contact.html")

def contact_messages(requset):
    
    if not requset.user.is_staff :
        messages.error(requset,"Only Admins Can See The Messages","alert-danger")
        return redirect("Main:home")
    
    messages_list = Contact.objects.all()
    
    return render(requset,"Main/contact_messages.html",{'messages_list':messages_list})

def about(request):
    return render(request,"Main/about.html")