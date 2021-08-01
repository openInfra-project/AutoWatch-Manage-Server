from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=128, verbose_name="아이디")
    username = models.CharField(max_length=64, verbose_name="사용자명")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registerd_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')
    image = models.ImageField(null=True, verbose_name='이미지')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'hasik_user'
        verbose_name = '사용자 명단'
        verbose_name_plural = '사용자 명단'  # 복수명 설정
