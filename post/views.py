from django.shortcuts import render, redirect
from .models import Recipe, Timecate, Diffcate
from .forms import *
from django.http import HttpResponse
from post.models import Recipe
# Create your views here.



def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/signin')

def view_main(request):
    return render(request,'main.html')

def view_search(request):
    total_recipe = Recipe.objects.count()
    recipe = Recipe.objects.all()
    all_recipe = Recipe.objects.all()

    timecost = ["10분", "20분", "30분", "60분"]
    difficulty = ["상", "중", "하"]
    doc = {
        'recipes': all_recipe,
        'new_recipe': recipe,
        'timecost': timecost,
        'difficulty': difficulty,
    }

    if request.method == 'GET':
        return render(request, 'list.html', doc)
    elif request.method == 'POST':
        searched = request.POST.get('searched', '')

        search_list= []
        for i in range(total_recipe):
            title = Recipe.objects.all().values()[i]['title'] #제목 꺼내오기
            if searched in title:#타이틀에 내가 원하는 이름이 있다면
                search_list.append(Recipe.objects.all().values()[i])#내가 원하는 데이터 만으로 쿼리셋으로 만든다

        doc['searched'] = searched #앞에서 선언해준 doc에 새로 만든 키값을 추가한다다
        doc['search_list'] = search_list

        return render(request, 'list.html', doc)


def view_filter(request):
    if request.method == 'POST':
        timecost_value = request.POST.get('timecost','')
        difficulty_value = request.POST.get('difficulty', '')

        recipe = Recipe.objects.all()
        all_recipe = Recipe.objects.all()

        ten_min = Recipe.objects.filter(difficulty="10분 이내").values()
        twenty_min = Recipe.objects.filter(difficulty="20분 이내").values()
        thirty_min = Recipe.objects.filter(difficulty="30분 이내").values()
        sixty_min = Recipe.objects.filter(difficulty="60분 이내").values()
        difficult = Recipe.objects.filter(timecost="중급").values()
        soso = Recipe.objects.filter(timecost="초급").values()
        easy = Recipe.objects.filter(timecost="아무나").values()

        timecost = ["10분", "20분", "30분", "60분"]
        difficulty = ["상", "중", "하"]

        if timecost_value == "10분":
            filter_value = ten_min
        elif timecost_value == "20분":
            filter_value = twenty_min
        elif timecost_value == "30분":
            filter_value = thirty_min
        elif timecost_value == "60분":
            filter_value = sixty_min
        elif difficulty_value == "상":
            filter_value = difficult
        elif difficulty_value == "중":
            filter_value = soso
        elif difficulty_value == "하":
            filter_value = easy


        doc = {
            'recipes': all_recipe,
            'new_recipe': recipe,
            'timecost': timecost,
            'difficulty': difficulty,
            'filter_value': filter_value
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
        return redirect('/')
