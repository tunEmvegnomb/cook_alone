from django.shortcuts import render, redirect
from .models import Recipe, Timecate, Diffcate
from .forms import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    return redirect('list/')

def view_list(request):
    if request.method == 'GET':
        recipe = Recipe.objects.all()
        return render(request, 'list.html', {'recipe':recipe})


def upload_recipes(request):
    if request.method == 'GET':
        ur_user = request.user.is_authenticated
        if ur_user:
            timecate = Timecate.objects.all()
            diffcate = Diffcate.objects.all()
            return render(request, 'upload.html', {'timecost': timecate, 'difficulty': diffcate})
        else:
            return redirect('/')

    elif request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('list/')
        else:
            return HttpResponse('fail')



