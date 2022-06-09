from django.db import models
from user.models import UserModel
from post.models import Recipe

# Create your models here.
class LikeModel(models.Model):
    class Meta:
        db_table = 'like'

    like_me = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    like_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentModel(models.Model):
    class Meta:
        db_table = 'comment'

    comment_me = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
