from django.shortcuts import render, redirect
from .models import Timecate, Diffcate
from django.http import HttpResponse
# Create your views here.
def home(request):
    return redirect('list/')

def view_list(request):
    if request.method == 'GET':
        # recipe = Recipe.objects.all()
        # chucheon = RecipeChucheon.objects.all()
        # print(type(chucheon))
        return render(request, 'list.html')#, {'recipe':recipe})

def upload_recipes(request):
    if request.method == 'GET':
        # form = RecipeForm()
        timecate = Timecate.objects.all()
        diffcate = Diffcate.objects.all()
        return render(request, 'upload.html', {'timecost': timecate, 'difficulty': diffcate})