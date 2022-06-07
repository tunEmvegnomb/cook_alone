from django import forms #장고 forms라는 클래스를 상속해줄거임
from .models import *


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['author', 'title', 'img_url', 'ingredient', 'cookstep', 'difficulty', 'timecost']