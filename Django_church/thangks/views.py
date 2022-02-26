from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime


from .forms import ThanksForm





# 감사 기능
"""
수정과 같이 instance=user를 미리 지정해놓아서 저장이 제대로 되지 않았었던 것임
"""

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


@login_required
def thk_farm(request):
    return render(request, "thangks/thk_farm.html", {})