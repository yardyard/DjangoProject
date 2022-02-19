from django.contrib import admin
from .models import User, Thangks
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'email', 'is_active', 'is_staff' ,'is_superuser'
        ]


@admin.register(Thangks)
class ThangksAdmin(admin.ModelAdmin):
        list_display = [
        'author', 'created', 'caption_1', 'caption_2', 'caption_3' 
        ]
