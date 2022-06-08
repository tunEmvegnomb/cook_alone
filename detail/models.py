from django.db import models
from user.models import UserModel
from webScrapping.models import DefaultRecipe

# Create your models here.
class CommentModel(models.Model):
    class Meta:
        db_table = "comment"

    comment_me = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment_default_recipe = models.ForeignKey(DefaultRecipe, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)