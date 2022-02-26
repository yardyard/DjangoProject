from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    #path('', TemplateView.as_view(template_name='root.html'), name='root' ), # re_path를 사용하면 모든 주소에 매칭이 된다.),
    
    path('signup/', views.signup, name='signup'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('password_change/', views.password_change, name='password_change'),
    path('edit/', views.profile_edit, name='profile_edit'),

    

    # TODO: 유저별 저장된 감사 이용 url
    #re_path(r'^(?P<username>[\w.@+-]+)/thanks/$', views.thanks, name='thanks'), 

]  