from django.contrib import admin
from .models import Category,Game,Review,Publisher
from Main.models import Contact
from Auth.models import Profile

# Register your models here.

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Publisher)
admin.site.register(Contact)
admin.site.register(Profile)
