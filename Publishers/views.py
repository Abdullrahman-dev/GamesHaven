from django.shortcuts import render , redirect
from .forms import PublisherForm
from .models import Publisher
from Games.models import Game

# Create your views here.


def add_publisher(requset):
    if requset.method == "POST":
        publisher_form = PublisherForm(requset.POST,requset.FILES)
        if publisher_form.is_valid():
            publisher_form.save()
        else :
            print(publisher_form.errors)

        return redirect("Publisher:publishers")
    return render(requset,"publishers/add_publisher.html")



def publishers(requset):
    publishers = Publisher.objects.all()
    return render(requset,"publishers/publishers.html",{"publishers":publishers})



def publisher_detail(requset,publisher_id):

    publisher = Publisher.objects.get(pk=publisher_id)
    games = Game.objects.filter(publisher=publisher).order_by('-release_date')
    
    context = {
        "games": games,
        "publisher": publisher,
    }
    
    return render(requset, "publishers/publisher_detail.html", context)