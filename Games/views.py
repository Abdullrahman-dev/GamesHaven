from django.shortcuts import render,redirect
from .models import Game,Category,Review
from .forms import GameForm
from Publishers.models import Publisher
# Create your views here.

def create_game(requset):

    game_form = GameForm()
    categories = Category.objects.all()
    publishers = Publisher.objects.all()
    
    if requset.method == "POST":
        
        game_form = GameForm(requset.POST,requset.FILES)
        
        if game_form.is_valid():
            game_form.save()
            return redirect("Main:home")
        
        else :
            print("Not valid form")
    
    return render(requset,"Games/create.html",{"game_form":game_form,'RatingChoices':reversed(Game.RatingChoices.choices),'categories':categories,'publishers':publishers})


def game_detail(requset,game_id):
    game = Game.objects.get(pk=game_id)
    
    reviews = Review.objects.filter(game=game).order_by('-created_at')

    context = {
        "game": game,
        "reviews": reviews,
    }

    return render(requset, "Games/game_detail.html", context)


def game_update(requset,game_id):
    game = Game.objects.get(pk=game_id)
    categories = Category.objects.all()
    publishers = Publisher.objects.all()

    if requset.method == "POST":
        game_form = GameForm(instance=game, data=requset.POST, files=requset.FILES)
        if game_form.is_valid():
            game_form.save()
            return redirect("Games:game_detail", game_id)
    else:
        game_form = GameForm(instance=game)

    return render(requset,"Games/game_update.html",{
        "game":game,
        "game_form":game_form,
        'RatingChoices':reversed(Game.RatingChoices.choices),
        'categories':categories,
        'publishers':publishers,
    })



def game_delete(requset,game_id):
    
    game = Game.objects.get(pk=game_id)
    game.delete()
    
    return redirect("Main:home") 



def all_games(requset):

    games = Game.objects.all()

    return render(requset,"Games/all_games.html",{"games":games})



def search_games(requset):
    
    if "search" in requset.GET : # and len(requset.GET["search"]) >= 0 
        games = Game.objects.filter(title__contains=requset.GET["search"])

        if "sort" in requset.GET and requset.GET["sort"] == "rating_desc":
            games = Game.objects.all().order_by("-rating")

        elif "sort" in requset.GET and requset.GET["sort"] == "rating_asc":
            games = Game.objects.all().order_by("rating")

        elif "sort" in requset.GET and requset.GET["sort"] == "newest":
            games = Game.objects.all().order_by("-release_date")

        elif "sort" in requset.GET and requset.GET["sort"] == "oldest":
            games = Game.objects.all().order_by("release_date")

        elif "sort" in requset.GET and requset.GET["sort"] == "title_az":
            games = Game.objects.all().order_by("title")

        elif "sort" in requset.GET and requset.GET["sort"] == "title_za":
            games = Game.objects.all().order_by("-title")

        else:
            games = Game.objects.all()
        
    else :
        games = []
    
    return render(requset, "Games/search_games.html", {"games": games})


def add_review(requset,game_id):

    if requset.method == "POST":
        game = Game.objects.get(pk=game_id)
        new_reviews = Review(
            game = game,
            name = requset.POST["name"],
            comment = requset.POST["comment"],
            rating = requset.POST["rating"],
        )
        new_reviews.save()
        
    return redirect("Games:game_detail",game_id=game_id)