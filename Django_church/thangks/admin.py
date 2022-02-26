from django.contrib import admin
from .models import Thangks
# Register your models here.

@admin.register(Thangks)
class ThangksAdmin(admin.ModelAdmin):
        list_display = [
        'author', 'created', 'caption_1', 'caption_2', 'caption_3' 
        ]
