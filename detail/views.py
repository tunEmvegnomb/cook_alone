from django.shortcuts import render, redirect
from webScrapping.models import DefaultRecipe
from detail.models import LikeModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def view_detail(request, id):
    target_recipe = DefaultRecipe.objects.get(id=id)
    target_like = LikeModel.objects.filter(like_recipe=id)
    if target_like:
        like_status = True
    else:
        like_status = False
    return render(request, 'detail.html', {'recipe': target_recipe, 'like_status': like_status})

@login_required
def like_post(request, id):
    me = request.user
    recipe = DefaultRecipe.objects.get(id=id)
    target_like = LikeModel.objects.filter(like_me=me, like_recipe=recipe)
    if target_like:
       target_like.delete()
    else:
        target_like = LikeModel()
        target_like.like_me = me
        target_like.like_recipe = recipe
        target_like.save()
    return redirect(f'/detail/{id}')