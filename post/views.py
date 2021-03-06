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
        target_reco = RecommendModel.objects.get(id=2)


    reco_main = int((target_reco.reco1.strip('()').split(',')[0])) + 1
    reco_main = Recipe.objects.get(id=reco_main)
    reco_ing = reco_main.ingredient.split('>')[:5]


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
    return render(request, 'main.html', {'reco_main': reco_main, 'reco_recipes': reco_recipes, 'reco_ing':reco_ing})



def view_search(request):
    total = Recipe.objects.count()
    latest_num = Recipe.objects.latest('id').id
    # print(f'total->{total}')
    # print(f'latest_num->{latest_num}')
    all_recipes = Recipe.objects.get_queryset().order_by('-id').values('id', 'title', 'img_url', 'img_file', 'author_id')
    all_recipe = []
    # print(f'1->{all_recipes.filter(id=1)}')
    for index in range(1, latest_num+1):

        try:
            like_num = LikeModel.objects.filter(like_recipe_id=index).count()
            target_recipe = all_recipes.get(id=index)
            target_recipe['like_num'] = like_num
            all_recipe.append(target_recipe)

            if like_num == 1:
                # print(f'index,num->{index, like_num, target_recipe}')
                pass
        except:
            pass
    # print(f'target_recipes->{target_recipes}')
            # print(f'????????????->{index}')
    # all_recipes2 = Recipe.objects.get_queryset().order_by('id')

    # all_recipe = list(all_recipes2.values('id', 'title', 'img_url', 'img_file', 'author_id'))
    #
    # for index in range(1, latest_num+1):
    #     try:
    #         like_num = LikeModel.objects.filter(like_recipe_id=index).count()
    #         all_recipe[index-1]['like_num'] = like_num
    #         if like_num == 1:
    #             print(f'index,num->{index, like_num, Recipe.objects.filter(id=index)}')
    #
    #     except:
    #         pass

    searched=0

    try: #????????? ???????????? ????????? try
        #????????? ??? 1=> ????????? ????????????????
        if request.session['filter_type'] == "filters":
            if request.session['filter_name'] == "10???":
                filter_value = Recipe.objects.filter(timecost="10??? ??????").values()
            elif request.session['filter_name'] == "20???":
                filter_value = Recipe.objects.filter(timecost="20??? ??????").values()
            elif request.session['filter_name'] == "30???":
                filter_value = Recipe.objects.filter(timecost="30??? ??????").values()
            elif request.session['filter_name'] == "60???":
                filter_value = Recipe.objects.filter(timecost="60??? ??????").values()
            elif request.session['filter_name'] == "???":
                filter_value = Recipe.objects.filter(difficulty="??????").values()
            elif request.session['filter_name'] == "???":
                filter_value = Recipe.objects.filter(difficulty="??????").values()
            elif request.session['filter_name'] == "???":
                filter_value = Recipe.objects.filter(difficulty="?????????").values()
            elif request.session['filter_name'] == "most_popular":
                filter_value = sorted(all_recipe, key=lambda d: d['like_num'])
                filter_value.reverse()
            elif request.session['filter_name'] == "most_recent":
                filter_value = all_recipe
                filter_value.reverse()
            ###????????? ?????????????????? ?????????####
            using_recipes =filter_value
        # ????????? ??? 2=> ???????????? ????????????????
        elif request.session['filter_type'] == "searched":
            using_recipes = Recipe.objects.filter(title__contains=request.session['filter_name']) or Recipe.objects.filter(author__username__contains=request.session['filter_name'])
            searched=request.session['filter_name']

    # ????????? ??? 3=> ??? ??? ??????????????? ????????? all_recipe??? ??????
    except:
        using_recipes = all_recipe
        using_recipes.reverse()

    # <<<--- ?????????????????? --- #
    paginator = Paginator(using_recipes, 15)
    page_number = request.GET.get('page')
    p_recipe = paginator.page(page_number).object_list
    page_obj = paginator.page(page_number)
    # ????????? ????????? ?????? ?????????
    page_index = []
    page_digit = len(str(page_obj.number-1))
    # ????????????
    if page_digit == 1:
        page_firstNum = 0
    # ????????????
    if page_digit == 3:
        page_firstNum = int(str(page_obj.number-1)[:2])
        print(f'page 100~ {page_firstNum}')
    else:
        page_firstNum = int(str(page_obj.number - 1)[0])
    for page in range(1, 11):
        page = page_firstNum * 10 + page
        page_index.append(page)

    # --- ?????????????????? --->>> #

    timecost = ["10???", "20???", "30???", "60???"]
    difficulty = ["???", "???", "???"]
    doc = {
        'recipes': p_recipe,
        'timecost': timecost,
        'difficulty': difficulty,
        'page_obj': page_obj,
        'page_index': page_index,
        'searched': searched,
    }
    # NUMBER = doc['recipes'][0]['like_num']
    # RECIPE = doc['recipes'][0]
    # print(f'???????????????->{RECIPE}???????????? ??????->{NUMBER}')
    if request.method == 'GET':
        return render(request, 'list.html', doc)


# !!???????????? ?????? ??????????????????!!
def searching(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', '')
        #?????? ??????
        request.session['filter_name'] = searched
        request.session['filter_type'] = "searched"

        return redirect('/search/?page=1')


# !!???????????? ?????????!!
def view_filter(request):
    if request.method == 'POST':
        timecost_value = request.POST.get('timecost', '')
        difficulty_value = request.POST.get('difficulty', '')
        mostfilter_value = request.POST.get('most_filter', '')

        request.session['filter_name'] = timecost_value or difficulty_value or mostfilter_value
        request.session['filter_type'] = "filters"
        request.session['edit'] = True
        return redirect('/search/?page=1')


def upload_recipes(request):

    if request.method == 'GET':
        # print(f'?????? ?????? ?????? -> {request.session["update"]}')
        try:
            #????????? ?????????
            is_update = request.session['update']
            #???????????? ????????? ????????????
            print(f'?????? ???????????? -> {request.session["myrecipe"]}')
            target_recipe = Recipe.objects.get(id=request.session['myrecipe'])
            print(f'?????? ???????????? -> {target_recipe}')
        except:
            #????????? ?????????
            is_update = False
            target_recipe = ''
        ur_user = request.user.is_authenticated

        if ur_user:
            timecate = Timecate.objects.all()
            diffcate = Diffcate.objects.all()
            return render(request, 'upload.html',
                          {'timecost': timecate,
                           'difficulty': diffcate,
                           'is_update': is_update,
                           'target_recipe':target_recipe
                           })
        else:
            return redirect('/')

    elif request.method == 'POST':
        author = request.user
        title = request.POST.get('title', '')
        img_file = request.FILES.get('img_url', '')
        timecost = request.POST.get('timecost', '')
        difficulty = request.POST.get('difficulty', '')
        ingredient = request.POST.get('ingredient', '')
        cookstep = request.POST.get('cookstep', '')

        my_post = Recipe.objects.create(author=author, title=title, img_file=img_file, timecost=timecost,
                                        difficulty=difficulty, ingredient=ingredient, cookstep=cookstep)
        my_post.save()
        return redirect('/')
