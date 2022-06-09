from django.shortcuts import render, redirect
from webScrapping.models import DefaultRecipe
from detail.models import LikeModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CommentModel

# Create your views here.
def view_detail(request, id):
    target_recipe = DefaultRecipe.objects.get(id=id)
    target_like = LikeModel.objects.filter(like_recipe=id)
    all_comment = CommentModel.objects.filter(comment_recipe=id).order_by('-created_at')
    if target_like:
        like_status = True
    else:
        like_status = False
    return render(request, 'detail.html', {'recipe': target_recipe, 'like_status': like_status, 'comment':all_comment})

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

@login_required
def comment_post(request, id):
    if request.method == 'POST':
        me = request.user
        recipe = DefaultRecipe.objects.get(id=id)
        target_comment = CommentModel.objects.filter(comment_me = me, comment_recipe=recipe)
        comment_content = request.POST.get('comment','')

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
        'all_comment' : all_comment
    }
    return render(request, 'comment_update.html', context)


@login_required
def comment_update_end(request, id):

        all_comment = CommentModel.objects.get(id=id)
        target_recipe = all_comment.comment_recipe.id

        all_comment.comment_content = request.POST.get('comment_update')
        all_comment.save()
        print(all_comment.comment_content)
        return redirect(f'/detail/{target_recipe}')

