from distutils.command.upload import upload
from time import timezone
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.template.loader import render_to_string
from django.core.validators import RegexValidator



class User(AbstractUser):
    class TeamChoices(models.TextChoices):
        Male =  "공동체", "남성 공동체"
        FEMALE =  "여성 공동체", "여성 공동체"
        Young =  "젊은이 부", "젊은이 부"
        Teenager = "청소년부", "청소년부"
        Kids =  "아동부", "아동부"
    
    rema = models.TextField(blank=True, help_text="올해의 레마 말씀을 적어주세요!") 
    phone_number = models.CharField(blank=True, max_length=13, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    teamchoice = models.CharField(blank=True, max_length=8, choices=TeamChoices.choices
    , help_text="48px * 48px 크기의 png / jpg 파일을 업로드해주세요"
    )

    # upload_to="%Y/%m/%d" 는 업로드 되는 날짜에 따른 폴더가 생성이 된다.
    profile = models.ImageField(blank=True, upload_to="accounts/proflie/%Y/%m/%d")

    profile_message = models.TextField(blank=True, max_length=20)

    def send_welcome_email(self):        
        Subject = render_to_string("accounts/welcome_email_subjects.txt", {
            "user": self,
        })
        content = render_to_string("accounts/welcome_email_contents.txt", {
            "user": self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail( Subject, content , sender_email , [self.email], fail_silently=False)



class Thangks(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    caption_1 = models.TextField(blank=True, help_text="오늘 첫번째 감사한 내용을 적어주세요!")
    caption_2 = models.TextField(blank=True, help_text="오늘 두번째 감사한 내용을 적어주세요!")
    caption_3 = models.TextField(blank=True, help_text="오늘 세번째 감사한 내용을 적어주세요!")



""" TODO: thanks:detail view 구현하기
    def get_absolute_url(self): # redirect시 활용
            return reverse('accounts:thanks_detail', args=[self.id])


"""