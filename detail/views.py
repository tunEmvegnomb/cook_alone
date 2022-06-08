from django.shortcuts import render
from webScrapping.models import DefaultRecipe
from .models import CommentModel

# Create your views here.
def view_detail(request, id):
    if request.method == 'GET':
        target_recipe = DefaultRecipe.objects.get(id=id)
        return render(request, 'detail.html', {'recipe': target_recipe})

#댓글은 누구나 다 볼 수 있음
#댓글을 쓰려고하면 로그인을 했는지 확인해야함
#로그인을 했다면 댓글쓰는 창으로 돌아오고
#댓글을 쓴다면 댓글이 저장되어야함
