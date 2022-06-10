from django.db import models

# Create your models here.
class RecommendModel(models.Model):
    class Meta:
        db_table = 'default_reco'
    reco1 = models.CharField(max_length=100, blank=True)
    reco2 = models.CharField(max_length=100, blank=True)
    reco3 = models.CharField(max_length=100, blank=True)
    reco4 = models.CharField(max_length=100, blank=True)
    reco5 = models.CharField(max_length=100, blank=True)