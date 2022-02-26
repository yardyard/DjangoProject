from django import forms
from .models import Thangks
from datetime import timedelta
from django.utils import timezone

# 감사 폼
class ThanksForm(forms.ModelForm):
    class Meta:
        model = Thangks
        fields = [
            'caption_1', 'caption_2', 'caption_3'
            ]
    
    """
    TODO: 나중에 JS로 구현하기 
    
    # 만약 감사를 올린지 24시간 이내이면 오류 발생
    def clean_created(self):
        created = self.cleaned_data.get('created')
        timesince = timezone.now() - timedelta(days=1)
        
        # 만약 감사를 올린지 24시간 이내이면 오류 발생
        if created:
            qs = Thangks.objects.all()\
            .filter(author=self.user.pk)\
            .filter(created__lte = timesince)  
            
            if qs.exists():
                raise forms.ValidationError("24시간 내에 감사를 등록했습니다..")
                
            return qs
    """