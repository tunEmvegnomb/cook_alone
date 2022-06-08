from django.db import models
from user.models import UserModel
from webScrapping.models import DefaultRecipe

# Create your models here.
class LikeModel(models.Model):
    class Meta:
        db_table='like'
    like_me = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    like_recipe = models.ForeignKey(DefaultRecipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)