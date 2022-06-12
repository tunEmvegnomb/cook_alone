from .models import Recipe, Timecate, Diffcate
from detail.models import LikeModel
from post.models import Recipe
from recommend.models import RecommendModel
from user.models import UserModel
from django.core.paginator import Paginator
from django.shortcuts import render,redirect


# Create your views here.
# def pagenating(request_list):

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/signin')


def view_main(request):
    try:
        target_reco = RecommendModel.objects.get(id=request.session['latestRecipe'])
    except:
        target_reco = RecommendModel.objects.get(id=1)


    reco_main = int((target_reco.reco1.strip('()').split(',')[0])) + 1
    reco_main = Recipe.objects.get(id=reco_main)
    reco_list = []
    reco_list.append(int(target_reco.reco2.strip('()').split(',')[0]) + 1)
    reco_list.append(int(target_reco.reco3.strip('()').split(',')[0]) + 1)
    reco_list.append(int(target_reco.reco4.strip('()').split(',')[0]) + 1)
    reco_list.append(int(target_reco.reco5.strip('()').split(',')[0]) + 1)
    reco_recipes = []
    for reco_num in reco_list:
        reco_recipe = Recipe.objects.get(id=reco_num)
        reco_recipes.append(reco_recipe)
    print(f'reco_recipes->{reco_recipes}')
    return render(request, 'main.html', {'reco_main': reco_main, 'reco_recipes': reco_recipes})



def view_search(request):
    total = Recipe.objects.count()
    # recipes = Recipe.objects.all()
    # print(total)
    # print(request.session['filter_name'])
    # print(request.session['filter_type'])




    #경수의 수1. 일반적인 경우의 수
    all_recipes = Recipe.objects.get_queryset().order_by('-id')

    all_recipe = list(all_recipes.values('id', 'title', 'img_url', 'img_file', 'author_id'))
    # !!카드 속 좋아요, 작성자 보이기!!
    # for a in range(total):
    for index, recipe in enumerate(all_recipe):
        # print(f'index->{index}, recipe->{recipe}')
        num = LikeModel.objects.filter(like_recipe_id=index).count()
        # if index <=total:
        all_recipe[total-index-1]['like_num'] = num

    # print(all_recipe)

        # id = all_recipe[index]['author_id']
        # try:
        #     author = UserModel.objects.get(id=id)
        #     author = str(author)
        # except:
        #     author = "혼자서도 잘해요리"
        # all_recipe[index]['author'] = author
    try:
        if request.session['filter_type'] == "filters":


            if request.session['filter_name']== "10분":
                filter_value = Recipe.objects.filter(timecost="10분 이내").values()
            elif request.session['filter_name'] == "20분":
                filter_value = Recipe.objects.filter(timecost="20분 이내").values()
            elif request.session['filter_name'] == "30분":
                filter_value = Recipe.objects.filter(timecost="30분 이내").values()
            elif request.session['filter_name'] == "60분":
                filter_value = Recipe.objects.filter(timecost="60분 이내").values()
            elif request.session['filter_name'] == "상":
                filter_value = Recipe.objects.filter(difficulty="중급").values()
            elif request.session['filter_name'] == "중":
                filter_value = Recipe.objects.filter(difficulty="초급").values()
            elif request.session['filter_name'] == "하":
                filter_value = Recipe.objects.filter(difficulty="아무나").values()
            elif request.session['filter_name'] == "most_popular":
                filter_value = sorted(all_recipe, key=lambda d: d['like_num'])
                filter_value.reverse()
                print(filter_value[2])
                # all_recipe = list(all_recipes.values('id', 'title', 'img_url', 'img_file', 'author_id'))
                # for i in all_recipe:
                #
            elif request.session['filter_name'] == "most_recent":
                filter_value = all_recipe
            #필터를 사용했을때의 결과값
            using_recipes =filter_value
        elif request.session['filter_type'] == "searched":
            using_recipes = Recipe.objects.filter(title__contains=request.session['filter_name'])

    except:
        using_recipes = all_recipe

    # <<<--- 페이지네이션 --- #
    paginator = Paginator(using_recipes, 15)
    page_number = request.GET.get('page')
    p_recipe = paginator.page(page_number).object_list
    page_obj = paginator.page(page_number)
    print(page_obj)
    # 페이지 인덱스 번호 구하기
    page_index = []
    page_digit = len(str(page_obj.number-1))
    print(page_digit)
    if page_digit == 1:
        page_firstNum = 0
    else:
        page_firstNum = int(str(page_obj.number - 1)[0])
    for page in range(1, 11):
        page = page_firstNum * 10 + page
        page_index.append(page)

    # --- 페이지네이션 --->>> #


    # all_recipe.reverse()

    # !!최신순, 인기순 필터 만들기!!
    # like_sort_list = sorted(all_recipe, key=lambda d: d['like_num'])
    # like_sort_list.reverse()

    timecost = ["10분", "20분", "30분", "60분"]
    difficulty = ["상", "중", "하"]
    doc = {
        'recipes': p_recipe,
        'timecost': timecost,
        'difficulty': difficulty,
        # 'like_sort_list': like_sort_list,
        'page_obj': page_obj,
        'page_index':page_index
    }
    # print(f'페이지->{page_number}, 리스트->{all_recipes}')

    if request.method == 'GET':
        # print(f'doc-->{doc}')
        return render(request, 'list.html', doc)


# !!서치기능 새로 만들기ㅜㅜㅜ!!
def searching(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', '')
        search_list = []
        #!!검색기능 만들기!!
        total = Recipe.objects.count()
        for i in range(total):
            title = Recipe.objects.all().values()[i]['title']  # 제목 꺼내오기

            if searched in title:  # 타이틀에 내가 원하는 이름이 있다면
                search_list.append(Recipe.objects.all().values()[i])  # 내가 원하는 데이터 만으로 쿼리셋으로 만든다
        request.session['filter_name'] = searched
        request.session['filter_type'] = "searched"

        return redirect('/search/?page=1')


# !!필터기능 만들기!!
def view_filter(request):
    if request.method == 'POST':
        timecost_value = request.POST.get('timecost', '')
        difficulty_value = request.POST.get('difficulty', '')
        mostfilter_value = request.POST.get('most_filter', '')

        request.session['filter_name'] = timecost_value or difficulty_value or mostfilter_value
        request.session['filter_type'] = "filters"
        print(request.session['filter_name'])##most_popular

        return redirect('/search/?page=1')


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
