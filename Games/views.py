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



def search_games(request):
    
    search_query = request.GET.get("search", "")
    sort_option = request.GET.get("sort", "")

    games = Game.objects.filter(title__icontains=search_query)

    if sort_option == "rating_desc":
        games = games.order_by("-rating")
    elif sort_option == "rating_asc":
        games = games.order_by("rating")
    elif sort_option == "newest":
        games = games.order_by("-release_date")
    elif sort_option == "oldest":
        games = games.order_by("release_date")
    elif sort_option == "title_az":
        games = games.order_by("title")
    elif sort_option == "title_za":
        games = games.order_by("-title")

    return render(request, "Games/search_games.html", {"games": games})



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