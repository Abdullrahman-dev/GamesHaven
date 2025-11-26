from django import forms
from Games.models import Game

# Creating the form for class :
class GameForm(forms.ModelForm):
    class Meta :
        model = Game
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput({"class":"form-control"})
        }