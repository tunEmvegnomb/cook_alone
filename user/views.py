from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required

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
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, email=email, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            if email == '' or password == '':
                return render(request, 'signin.html',{'error' : '데이터를 전부 입력해주세요'})
            else:
                if me.email != email or me.password != password:
                    return render(request, 'signin.html',{'error' : '유저 네임 혹은 패스워드가 맞지 않습니다'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'signin.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')