from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from datetime import timedelta
from django.utils import timezone

from .models import Thangks
from .forms import ThanksForm



todaytimesince = timezone.now() - timedelta(days=1)

# 감사 기능

"""
Problem Solution
수정과 같이 instance=user를 미리 지정해놓아서 저장이 제대로 되지 않았었던 것임
"""
# 감사 추가
@login_required
def thk_new(request):

    if request.method == 'POST':
        form = ThanksForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created = datetime.datetime.now()
            form = post.save()
            messages.success(request, "오늘도 감사를 올린 성도님을 축복합니다." ) 
            return redirect('/')
   
    else:
        form = ThanksForm()
    
    return render(request, 'thangks/thanks_form.html', {
        'form' : form,
    })

# 감사 농장
@login_required
def thk_farm(request):

    # 오늘 올렸던 감사 목록
    today_thk = Thangks.objects.all()\
        .filter(author=request.user.pk)\
        .filter(created__gte = todaytimesince).last()
    
    
    monthtimesince = timezone.now() - timedelta(days=30)
    month_thk = Thangks.objects.all()\
        .filter(author=request.user.pk)\
        .filter(created__gte = monthtimesince)

        
    return render(request, "thangks/thk_farm.html", {
        "today_thk" : today_thk,
        "month_thk" : month_thk,
    })


# 오늘의 감사 수정 기능
@login_required
def thk_edit(request):
    
    # 오늘 올린 감사를 받아옵니다.
    today_thk = Thangks.objects.all()\
        .filter(author=request.user.pk)\
        .filter(created__gte = todaytimesince).last()

    # 받아온 오늘 올린 감사를 수정합니다.
    if request.method == 'POST':
        form = ThanksForm(request.POST, request.FILES, instance=today_thk)
        if form.is_valid():
            # form을 수정할 시간을 저장합니다.
            form.created = timezone.now()
            form.save()
            messages.success(request, "오늘의 감사가 수정되었습니다!") # TODO:일정 시간후에 알람 꺼지게 JS로 구현
            return redirect('thk_farm')
    else:
        form = ThanksForm(instance=today_thk)
    
    return render(request, 'thangks/thk_edit_form.html', {
        'form' : form,
    })