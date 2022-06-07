from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return redirect('list/')

def view_list(request):
    if request.method == 'GET':
        # recipe = Recipe.objects.all()
        # chucheon = RecipeChucheon.objects.all()
        # print(type(chucheon))
        return render(request, 'list.html')#, {'recipe':recipe})
