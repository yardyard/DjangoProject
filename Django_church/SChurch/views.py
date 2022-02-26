from django.shortcuts import render, redirect
from thangks.models import Thangks
from accounts.models import User
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model

import random

rand_user_list = []

last_user_pk = User.objects.count() -1
  
for _ in range(last_user_pk):
  a = random.randint(0,last_user_pk)
  while a in rand_user_list:
    a = random.randint(0,last_user_pk)
  rand_user_list.append(a)

def root(request):
    # filter는 값을 다 가져옴
    #thks = Thangks.objects.filter(author=request.user.pk)
    
    # get은 값을 한개만 가져옴
    #thks = Thangks.objects.get(author=request.user.pk)
    
    # first는 처음 값, last는 마지막 값을 가져옴 #https://velog.io/@magnoliarfsit/ReDjango-7.-ORM%EA%B3%BC-Queryset
    timesince = timezone.now() - timedelta(days=1)

    thk = Thangks.objects.all()\
      .filter(author=request.user.pk)\
      .filter(created__gte = timesince)[0]    
    
    # 랜덤 유저 감사 표시
    
    thk_user_0 = Thangks.objects.all()\
      .filter(author=rand_user_list[0]).last()
       
    thk_user_1 = Thangks.objects.all()\
      .filter(author=rand_user_list[1]).last()
 
    thk_user_2 = Thangks.objects.all()\
      .filter(author=rand_user_list[2]).last()
    
    thk_user_3 = Thangks.objects.all()\
      .filter(author=rand_user_list[3]).last()
    
    thk_user_4 = Thangks.objects.all()\
      .filter(author=rand_user_list[4]).last()

    return render(request, 'root.html', {
    'thk' : thk,
    'thk_user_0' : thk_user_0,
    'thk_user_1' : thk_user_1,
    'thk_user_2' : thk_user_2,
    'thk_user_3' : thk_user_3,
    'thk_user_4' : thk_user_4,
    })

