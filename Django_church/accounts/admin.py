from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'email', 'nickname', 'is_active', 'is_staff' ,'is_superuser'
        ]