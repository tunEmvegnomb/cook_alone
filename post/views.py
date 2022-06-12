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
    all_recipes = Recipe.objects.get_queryset().order_by('-id')
    all_recipe = list(all_recipes.values('id', 'title', 'img_url', 'img_file', 'author_id'))


    #좋아요수 보여야 하니까 all_recipe에 like_num넣기
    for index, recipe in enumerate(all_recipe):
        num = LikeModel.objects.filter(like_recipe_id=index).count()
        all_recipe[total-index-1]['like_num'] = num

    try: #세션이 들어온게 있는지 try
        #경우의 수 1=> 필터를 사용했는가?
        if request.session['filter_type'] == "filters":
            if request.session['filter_name'] == "10분":
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

            elif request.session['filter_name'] == "most_recent":
                filter_value = all_recipe
            #필터를 사용했을때의 결과값
            using_recipes =filter_value
        # 경우의 수 2=> 서치바를 사용했는가?
        elif request.session['filter_type'] == "searched":
            using_recipes = Recipe.objects.filter(title__contains=request.session['filter_name'])
    # 경우의 수 3=> 둘 다 아닐때에는 기존의 all_recipe를 반환
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

    if request.method == 'GET':
        return render(request, 'list.html', doc)


# !!서치기능 새로 만들기ㅜㅜㅜ!!
def searching(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', '')

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
