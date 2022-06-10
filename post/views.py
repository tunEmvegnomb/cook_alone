from django.shortcuts import render, redirect
from .models import Recipe, Timecate, Diffcate
from detail.models import LikeModel
from user.models import UserModel
from recommend.models import RecommendModel
# Create your views here.



def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/signin')

def view_main(request):
    target_reco = RecommendModel.objects.get(id=35)
    target_reco = target_reco.reco1
    target_reco = int(target_reco.strip('()').split(',')[0]) + 1
    target_reco = Recipe.objects.get(id=target_reco)
    # target_reco = Recipe.objects.get(id=target_reco)
    # print(f'그래서 레시피는 뭔데? ->{target_reco}')
    reco_ing = target_reco.ingredient.split('>')
    del reco_ing[-1]
    # print(reco_ing)
    return render(request,'main.html', {'reco': target_reco, 'reco_ing':reco_ing})


def view_search(request):
    total = Recipe.objects.count()
    recipes = Recipe.objects.all()

    all_recipe = list(recipes.values('id','title','img_url','img_file', 'author_id'))
    for a in range(total):
        num = LikeModel.objects.filter(like_recipe_id=a+1).count()
        id = all_recipe[a]['author_id']

        try:
            author = UserModel.objects.get(id=id)
            author = str(author)
        except:
            author = "더 맛있는 레시피"

        all_recipe[a]['like_num']=num
        all_recipe[a]['author'] = author
    all_recipe.reverse()

    timecost = ["10분", "20분", "30분", "60분"]
    difficulty = ["상", "중", "하"]
    doc = {
        'recipes': all_recipe,
        'timecost': timecost,
        'difficulty': difficulty,
    }

    if request.method == 'GET':
        return render(request, 'list.html', doc)
    elif request.method == 'POST':
        searched = request.POST.get('searched', '')

        search_list = []

        # !!검색기능 만들기!!
        for i in range(total):
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
        img_file = request.FILES.get('img_url', '')
        timecost = request.POST.get('timecost', '')
        difficulty = request.POST.get('difficulty', '')
        ingredient = request.POST.get('ingredient', '')
        cookstep = request.POST.get('ingredient', '')


        my_post = Recipe.objects.create(author=author, title=title, img_file=img_file, timecost=timecost,
                                        difficulty=difficulty, ingredient=ingredient, cookstep=cookstep)
        my_post.save()
        return redirect('/')
