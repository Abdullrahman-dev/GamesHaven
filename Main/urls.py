from django.urls import path
from .import views

app_name = "Main"

urlpatterns = [
    path("",views.home,name="home"),
    # For Dark And Light Mode :
    path("mode/<mode>/",views.mode_view,name="mode_view"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path("contact/messages/",views.contact_messages,name="contact_messages"),
]
