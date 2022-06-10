from django.shortcuts import render, redirect
from .models import UserModel
from post.models import Recipe
from detail.models import CommentModel, LikeModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from post.models import Recipe

# Create your views here.

def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect ('/')
        else:
            return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2' '')

        if password != password2:
            return render(request, 'signup.html', {'error': '비밀번호가 맞지 않습니다'})
        else:
            if username == '' or password == '' or email == '':
                return render(request, 'signup.html', {'error': '데이터를 전부 입력해주세요'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'signup.html', {'error':'존재하는 사용자입니다'})

            exist_user = get_user_model().objects.filter(email=email)
            if exist_user:
                return render(request, 'signup.html',{'error':'존재하는 이메일입니다'})
            else:
                UserModel.objects.create_user(
                    username=username, password=password, email=email)
                return redirect('/signin')
        # return redirect('signin/', {'msg':'회원가입 성공'})

def sign_in_view(request):
    if request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'signin.html',{'error':'유저 이름 혹은 패스워드를 입력해주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'signin.html')

@login_required #로그인 한 사용자만 접근 할 수 있게 해주는 기능
def logout(request):
    auth.logout(request)
    return redirect('/')


def myrecipe(request, id):
    if request.method == 'GET':
        user = request.user.is_authenticated #지금 요청을 보낸 사용자가 로그인이 되어 있는 사용자가 맞는지 알아보는 함수
        if user:
            me = request.user
            #내가 쓴 레시피 정보를 가져와서 보여줘야됨
            myrecipe = Recipe.objects.all()
            mycomment = CommentModel.objects.all()
            mylike = LikeModel.objects.all()

            return render(request, 'mypage.html', {'me': me, 'myrecipe': myrecipe, 'mycomment' : mycomment, 'mylike' : mylike})

        else:
            return render(request, 'signin.html')