from django.shortcuts import render, redirect
from thangks.models import Thangks
from accounts.models import User
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

import random




# root 페이지에 들어갈 함수들

def root(request):
    """
     filter는 값을 다 가져옴
    thks = Thangks.objects.filter(author=request.user.pk)
    
     get은 값을 한개만 가져옴
    thks = Thangks.objects.get(author=request.user.pk)
    
     first는 처음 값, last는 마지막 값을 가져옴 #https://velog.io/@magnoliarfsit/ReDjango-7.-ORM%EA%B3%BC-Queryset
    """
    
    timesince = timezone.now() - timedelta(days=1)
    
    # 만약 유저가 로그인 되었다면 thk에 쿼리셋 적용하기
    if request.user.is_authenticated:
      thk = Thangks.objects.all()\
        .filter(author=request.user.pk)\
        .filter(created__gte = timesince)[0]    
    else:
      thk = None

    # 랜덤 유저 감사 표시

    # 랜덤 유저 pk를 담을 리스트
    rand_user_list = []

    # 총 유저 수
    last_user_pk = User.objects.count() -1
    
    # 오늘 감사를 올릴 성도님 수    
    thk_today_cnt = Thangks.objects.all()\
      .filter(created__gte = timesince)    
   
    thk_today_user = thk_today_cnt.count()
    

    # 랜덤으로 중복되지 않게 pk 리스트에 추가
    for _ in range(last_user_pk):
      a = random.randint(0,last_user_pk)
      while a in rand_user_list:
        a = random.randint(0,last_user_pk)
      rand_user_list.append(a)
    
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

    thk_user_5 = Thangks.objects.all()\
      .filter(author=rand_user_list[5]).last()
    
    return render(request, 'root.html', {
    'last_user_pk' : last_user_pk,
    'thk_today_user' : thk_today_user,

    'thk' : thk,


    'thk_user_0' : thk_user_0,
    'thk_user_1' : thk_user_1,
    'thk_user_2' : thk_user_2,
    'thk_user_3' : thk_user_3,
    'thk_user_4' : thk_user_4,
    'thk_user_5' : thk_user_5,
    })

