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

        return render(request, 'list.html', {'recipes': all_recipe, 'new_recipe':recipe})
    elif request.method == 'POST':
        searched = request.POST.get('searched', '')
        print(searched)
        all_recipe = DefaultRecipe.objects.all()
        print(all_recipe)

        search_list=[]
        for i in range(DefaultRecipe.objects.count()):
            title = DefaultRecipe.objects.all().values()[i]['title'] #제목 꺼내오기
            if searched in title:#타이틀에 내가 원하는 이름이 있다면
                search_list.append(DefaultRecipe.objects.all().values()[i])#내가 원하는 데이터 만으로 쿼리셋으로 만든다
        print(search_list[0:2])

        recipe = Recipe.objects.all()
        return render(request, 'list.html', {'recipes': all_recipe, 'new_recipe':recipe, 'searched':searched, 'search_list':search_list })






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
        author = request.user
        title = request.POST.get('title', '')
        img_url = request.FILES.get('img_url', '')
        timecost = request.POST.get('timecost', '')
        difficulty = request.POST.get('difficulty', '')
        ingredient = request.POST.get('ingredient', '')
        cookstep = request.POST.get('ingredient', '')


        my_post = Recipe.objects.create(author=author, title=title, img_url=img_url, timecost=timecost,
                                        difficulty=difficulty, ingredient=ingredient, cookstep=cookstep)
        my_post.save()
        return HttpResponse('success')