from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import login as auth_login

from .forms import SignupForm
# Create your views here.



# 회원가입
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            next_url = request.GET.get('next', '/') # next 인자를 가져오고, 없으면 / 주소로 이동
            user = form.save()
            auth_login(request, user)
            messages.success(request, "회원가입이 되었습니다~!")
            return redirect(next_url)
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup_form.html', {
        'form' : form,
    })


# 로그인
login = LoginView.as_view(template_name="accounts/login_form.html")


# 로그아웃
def logout(request):
    messages.success(request, '로그아웃 되었습니다')
    return logout_then_login(request)