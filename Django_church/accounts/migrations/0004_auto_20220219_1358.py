# Generated by Django 3.2.12 on 2022-02-19 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220218_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='website_url',
        ),
        migrations.AlterField(
            model_name='user',
            name='teamchoice',
            field=models.CharField(blank=True, choices=[('공동체', '남성 공동체'), ('여성 공동체', '여성 공동체'), ('젊은이 부', '젊은이 부'), ('청소년부', '청소년부'), ('아동부', '아동부')], help_text='48px * 48px 크기의 png / jpg 파일을 업로드해주세요', max_length=8),
        ),
    ]