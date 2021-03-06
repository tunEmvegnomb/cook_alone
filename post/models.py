from django.db import models
from user.models import UserModel

#Create your models here.
class Recipe(models.Model):
    class Meta:
        db_table = "recipe"
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100, null=False)
    img_url = models.URLField(max_length=300, null=False, default='')
    timecost = models.CharField(max_length=10, null=True)
    difficulty = models.CharField(max_length=10, null=False) #SET_NULL:필드값이 사라지면 Null로 바꾼다. null=True일때만 사용할 수 있다
    ingredient = models.TextField(null=False)
    cookstep = models.TextField(null=False)
    ##여기까지 form##
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    img_file = models.ImageField(upload_to='uploads/', null=True)#CharField(max_length=200, default='')



class Timecate(models.Model):
    class Meta:
        db_table = "timecost"
    def __str__(self):
        return self.timecost
    timecost = models.CharField(max_length=50, default='')

class Diffcate(models.Model):
    class Meta:
        db_table = "difficulty"
    def __str__(self):
        return self.difficulty
    difficulty = models.CharField(max_length=50, default='')
