from django.shortcuts import render, redirect
from detail.models import LikeModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CommentModel
from post.models import Recipe
from recommend.models import RecommendModel


# Create your views here.
def view_detail(request, id):
    target_recipe = Recipe.objects.get(id=id)
    target_like = LikeModel.objects.filter(like_recipe=id)
    all_comment = CommentModel.objects.filter(comment_recipe=id).order_by('-created_at')
    try:
        target_reco = RecommendModel.objects.get(id=id)
    except:
        target_reco = RecommendModel.objects.get(id=100)
    reco_list = []
    reco_list.append(int(target_reco.reco1.strip('()').split(',')[0]) + 1)
    reco_list.append(int(target_reco.reco2.strip('()').split(',')[0]) + 1)
    reco_list.append(int(target_reco.reco3.strip('()').split(',')[0]) + 1)
    reco_list.append(int(target_reco.reco4.strip('()').split(',')[0]) + 1)
    reco_list.append(int(target_reco.reco5.strip('()').split(',')[0]) + 1)
    reco_recipes = []
    for reco_num in reco_list:
        reco_recipe = Recipe.objects.get(id=reco_num)
        reco_recipes.append(reco_recipe)
    try:
        request.session['latestRecipe'] = str(target_recipe.id)
    except:
        request.session['latestRecipe'] = 1
    # print(request.session['latestRecipe'])

    # 타겟 재료 정제
    target_ing = target_recipe.ingredient
    target_ing = target_ing.split('>')
    del target_ing[-1]

    # 타겟 순서 정제
    target_step = target_recipe.cookstep
    target_step = target_step.split('>')
    del target_step[-1]
    print(f'target_step->{target_step}')
    if target_like:
        like_status = True
    else:
        like_status = False
    return render(request, 'detail.html', {
        'recipe': target_recipe,
        'like_status': like_status,
        'comment': all_comment,
        'ing_list': target_ing,
        'cookstep_list': target_step,
        'reco_list': reco_recipes
    })


@login_required
def like_post(request, id):
    me = request.user
    recipe = Recipe.objects.get(id=id)
    target_like = LikeModel.objects.filter(like_me=me, like_recipe=recipe)
    if target_like:
        target_like.delete()
    else:
        target_like = LikeModel()
        target_like.like_me = me
        target_like.like_recipe = recipe
        target_like.save()
    return redirect(f'/detail/{id}')


@login_required
def comment_post(request, id):
    if request.method == 'POST':
        me = request.user
        recipe = Recipe.objects.get(id=id)
        target_comment = CommentModel.objects.filter(comment_me=me, comment_recipe=recipe)
        comment_content = request.POST.get('comment', '')

        makecomment = CommentModel()
        makecomment.comment_me = me
        makecomment.comment_recipe = recipe
        makecomment.comment_content = comment_content
        makecomment.save()
        return redirect(f'/detail/{id}')


@login_required
def comment_delete(request, id):
    all_comment = CommentModel.objects.get(id=id)
    target_recipe = all_comment.comment_recipe.id
    all_comment.delete()
    return redirect(f'/detail/{target_recipe}')


@login_required
def comment_update(request, id):
    all_comment = CommentModel.objects.get(id=id)
    context = {
        'all_comment': all_comment
    }
    return render(request, 'detail.html', context)


@login_required
def comment_update_end(request, id):
    all_comment = CommentModel.objects.get(id=id)
    target_recipe = all_comment.comment_recipe.id

    all_comment.comment_content = request.POST.get('comment_update')
    all_comment.save()
    print(all_comment.comment_content)
    return redirect(f'/detail/{target_recipe}')

###풀 리퀘스트가 안되서 혹시 몰라 낙서합니다!!ㅎㅎ
