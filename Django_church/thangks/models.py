from time import timezone
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.template.loader import render_to_string
from django.core.validators import RegexValidator


class Thangks(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=False)
    created = models.DateTimeField(auto_now_add=True)
    caption_1 = models.TextField(blank=True, help_text="오늘 첫번째 감사한 내용을 적어주세요!")
    caption_2 = models.TextField(blank=True, help_text="오늘 두번째 감사한 내용을 적어주세요!")
    caption_3 = models.TextField(blank=True, help_text="오늘 세번째 감사한 내용을 적어주세요!")




"""
    TODO: thanks:detail view 구현하기
    def get_absolute_url(self): # redirect시 활용
            return reverse('accounts:thanks_detail', args=[self.id])

"""