from dataclasses import field, fields
from datetime import timezone
import datetime
from .models import User, Thangks
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm

# 회원가입 폼
class SignupForm(UserCreationForm):
    # 회원가입시 새로운 필드들을 커스텀 하고 싶을 때 생성자 호출
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) # 부모를 호출함.
        # form에 적용시키고 싶은 필드들을 오버라이딩을 통해 True로 지정
        self.fields['profile'].required = True
        self.fields['rema'].required = True
        self.fields['phone_number'].required = True     
        self.fields['teamchoice'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username', 'profile', 'rema', 'phone_number', 'teamchoice'
        ]
    
    # email 중복 방지 함수
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
            
            return email

# 프로필 수정 폼
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'profile', 'profile_message', 'rema', 'phone_number', 'teamchoice'   
        ]


# 비밀번호 수정 폼
class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password1(self):
        # 기존 암호
        old_password = self.cleaned_data.get('old_password')
        
        # 새로운 암호
        new_password1 = self.cleaned_data.get('new_password1')
        
        # 만약 기존 암호와 새로운 암호가 같다면
        if old_password and new_password1:    
            if old_password == new_password1:
                raise forms.ValidationError("변경할 암호가 기존 암호와 달라야 합니다")
        
        return new_password1


# 감사 폼
class ThanksForm(forms.ModelForm):
    class Meta:
        model = Thangks
        fields = [
            'caption_1', 'caption_2', 'caption_3'
            ]
    
    
    # 만약 감사를 올린지 24시간 이내이면 오류 발생
    def clean_created(self):
        created = self.cleaned_data.get('created')

        # 만약 감사를 올린지 24시간 이내이면 오류 발생
        if created:
            qs = User.objects.filter(created = datetime.datetime.now() - datetime.timedelta(hours=23))
            if qs.exists():
                raise forms.ValidationError("24시간 내에 감사를 등록했습니다..")
                
            return qs
