from django.urls import path
from .import views

app_name = "Auth"

urlpatterns = [
    path("registration/",views.registration,name="registration"),
    path("login/",views.loginn,name="loginn"),
    path("logout/",views.logoutt,name="logoutt"),
    path("profile/<user_id>",views.profile,name="profile"),
]