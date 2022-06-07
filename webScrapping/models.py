from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class DefaultRecipe(models.Model):
    class Meta:
        db_table = "default_recipe"
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100, null=False)
    img_url = models.URLField(max_length=200)
    timecost = models.CharField(max_length=30, null=False)
    difficulty = models.CharField(max_length=30, null=False) #SET_NULL:필드값이 사라지면 Null로 바꾼다. null=True일때만 사용할 수 있다
    ingredient = models.TextField(null=False)
    cookstep = models.TextField(null=False)