from django.shortcuts import render,redirect
from Games.models import Game , Category

# Create your views here.


def home(request):
    
    games = Game.objects.all()[0:3]
    # FIX: Changed from a set {"games", games} to a dictionary {"games": games}
    return render(request,"Main/home.html",{"games": games})

# For Dark And Light Mode :
def mode_view(request,mode):
    response = redirect(request.GET.get("next","/"))
    if mode == "light":
        response.set_cookie("mode","light")
    elif mode == "dark":
        response.set_cookie("mode","dark")
    return response
    
def contact(request):
    return render(request,"Main/contact.html")

def about(request):
    return render(request,"Main/about.html")