from django.urls import path, re_path
from . import views


urlpatterns = [
    path('thk/new/', views.thk_new, name='thk_new'),
    path('thk/farm/', views.thk_farm, name='thk_farm'),
    path('thk/farm/edit/', views.thk_edit, name='thk_edit'),
]