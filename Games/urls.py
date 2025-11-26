from django.urls import path
from .import views

app_name = "Games"

urlpatterns = [
    path("create/", views.create_game,name="create_game"),
    path("detail/<game_id>/",views.game_detail,name="game_detail"),
    path("update/<game_id>/",views.game_update,name="game_update"),
    path("delete/<game_id>/",views.game_delete,name="game_delete"),
    path("all/",views.all_games,name="all_games"),
    path("search/",views.search_games,name="search_games"),
    path("reviews/add/<game_id>/",views.add_review,name="add_review")
]
