from django.contrib import admin
from .models import Category,Game,Review,Publisher

# Register your models here.

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Publisher)