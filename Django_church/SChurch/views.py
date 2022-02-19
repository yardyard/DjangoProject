import datetime
from time import time, timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, logout_then_login, PasswordChangeView as AuthPasswordChangeView
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from accounts.models import User ,Thangks

def root(request):
    # filter는 값을 다 가져옴
    #thks = Thangks.objects.filter(author=request.user.pk)
    
    # get은 값을 한개만 가져옴
    #thks = Thangks.objects.get(author=request.user.pk)
    
    # first는 처음 값, last는 마지막 값을 가져옴 #https://velog.io/@magnoliarfsit/ReDjango-7.-ORM%EA%B3%BC-Queryset
    thk = Thangks.objects.filter(author=request.user.pk)
    
    return render(request, 'root.html', {
    'thk' : thk,
    })

  
  
  
  


    """
                    {% for thk in thks %}
                      <li><i class="bi bi-emoji-heart-eyes"></i> <strong>감사</strong> <span>{{ thk.caption_1 }}</span></li>
                      <li><i class="bi bi-emoji-heart-eyes"></i> <strong>감사</strong> <span>{{ thk.caption_2 }}</span></li>
                      <li><i class="bi bi-emoji-heart-eyes"></i> <strong>감사</strong> <span>{{ thk.caption_3 }}</span></li>
                    {% endfor %}
    """