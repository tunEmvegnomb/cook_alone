from django.shortcuts import render, redirect
from .models import Recipe, Timecate, Diffcate
from .forms import *
from django.http import HttpResponse
from webScrapping.models import DefaultRecipe

# Create your views here.



def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/search')
    else:
        return redirect('/signin')

def view_search(request):
    total_recipe = DefaultRecipe.objects.count()
    recipe = Recipe.objects.all()
    all_recipe = DefaultRecipe.objects.all()

    ten_min = DefaultRecipe.objects.filter(difficulty="10분 이내").values()
    twenty_min = DefaultRecipe.objects.filter(difficulty="20분 이내").values()
    thirty_min = DefaultRecipe.objects.filter(difficulty="30분 이내").values()
    sixty_min = DefaultRecipe.objects.filter(difficulty="60분 이내").values()
    difficult = DefaultRecipe.objects.filter(timecost="중급").values()
    soso = DefaultRecipe.objects.filter(timecost="초급").values()
    easy = DefaultRecipe.objects.filter(timecost="아무나").values()

    timecost = ["10분", "20분", "30분", "60분"]
    difficulty = ["상", "중", "하"]
    doc = {
        'recipes': all_recipe,
        'new_recipe': recipe,
        'ten_min': ten_min,
        'twenty_min': twenty_min,
        'thirty_min': thirty_min,
        'sixty_min': sixty_min,
        'difficult': difficult,
        'soso': soso,
        'easy': easy,
        'timecost': timecost,
        'difficulty': difficulty,
    }

    if request.method == 'GET':
        return render(request, 'list.html', doc)
    elif request.method == 'POST':
        searched = request.POST.get('searched', '')

        search_list= []
        for i in range(total_recipe):
            title = DefaultRecipe.objects.all().values()[i]['title'] #제목 꺼내오기
            if searched in title:#타이틀에 내가 원하는 이름이 있다면
                search_list.append(DefaultRecipe.objects.all().values()[i])#내가 원하는 데이터 만으로 쿼리셋으로 만든다

        doc['searched'] = searched #앞에서 선언해준 doc에 새로 만든 키값을 추가한다다
        doc['search_list'] = search_list

        return render(request, 'list.html', doc)


def view_filter(request):
    if request.method == 'POST':
        timecost_value = request.POST.get('timecost','')
        difficulty_value = request.POST.get('difficulty', '')
        print(timecost_value)
        print(difficulty_value)

        recipe = Recipe.objects.all()
        all_recipe = DefaultRecipe.objects.all()

        ten_min = DefaultRecipe.objects.filter(difficulty="10분 이내").values()
        twenty_min = DefaultRecipe.objects.filter(difficulty="20분 이내").values()
        thirty_min = DefaultRecipe.objects.filter(difficulty="30분 이내").values()
        sixty_min = DefaultRecipe.objects.filter(difficulty="60분 이내").values()
        difficult = DefaultRecipe.objects.filter(timecost="중급").values()
        soso = DefaultRecipe.objects.filter(timecost="초급").values()
        easy = DefaultRecipe.objects.filter(timecost="아무나").values()

        timecost = ["10분", "20분", "30분", "60분"]
        difficulty = ["상", "중", "하"]
        doc = {
            'recipes': all_recipe,
            'new_recipe': recipe,
            'ten_min': ten_min,
            'twenty_min': twenty_min,
            'thirty_min': thirty_min,
            'sixty_min': sixty_min,
            'difficult': difficult,
            'soso': soso,
            'easy': easy,
            'timecost': timecost,
            'difficulty': difficulty,
            'timecost_value': timecost_value,
            'difficulty_value': difficulty_value,
        }

        return render(request, 'list.html', doc)



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

