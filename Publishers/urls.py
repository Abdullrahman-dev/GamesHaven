from django.urls import path
from .import views

app_name = "Publisher"

urlpatterns = [
    path("add/",views.add_publisher,name="add_publisher"),
    path("",views.publishers,name="publishers"),
    path("detail/<publisher_id>/",views.publisher_detail,name="publisher_detail"),
]