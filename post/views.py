from django.shortcuts import render, redirect
from .models import Recipe, Timecate, Diffcate
from .forms import *
from django.http import HttpResponse
from webScrapping.models import DefaultRecipe

# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/list')
    else:
        return redirect('/signin')

def view_list(request):
    if request.method == 'GET':
        recipe = Recipe.objects.all()
        all_recipe = DefaultRecipe.objects.all()

        return render(request, 'list.html', {'recipes': all_recipe})

def upload_recipes(request):
    if request.method == 'GET':
        ur_user = request.user.is_authenticated
        if ur_user:
            timecate = Timecate.objects.all()
            diffcate = Diffcate.objects.all()
            return render(request, 'upload.html', {'timecost': timecate, 'difficulty': diffcate})
        else:
            return redirect('/')

    elif request.method == 'POST':
        author = request.user.username
        print(author)
        form = RecipeForm(request.POST, request.FILES)
        print("0번")

        print(form)
        if form.is_valid():
            print("1번")
            form.save()
            print("2번")

            return redirect('list/')
        else:
            return HttpResponse('fail')



