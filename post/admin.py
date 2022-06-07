from django.contrib import admin
from .models import Recipe, Timecate, Diffcate

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Timecate)
admin.site.register(Diffcate)
