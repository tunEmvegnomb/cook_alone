from django.shortcuts import render
from webScrapping.models import DefaultRecipe

# Create your views here.
def view_detail(request, id):
    target_recipe = DefaultRecipe.objects.get(id=id)

    return render(request, 'detail.html', {'recipe': target_recipe})