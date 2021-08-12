from django.db import models


class Room(models.Model):
    room_name = models.CharField(max_length=128, verbose_name="방 이름")
    room_password = models.CharField(max_length=64, verbose_name="방 비밀번호")
    file = models.FileField(upload_to="room", verbose_name="파일", default="NULL")
    mode = models.CharField(max_length=64, verbose_name="모드", default="NULL")
    maker = models.EmailField(max_length=64, verbose_name="생성자", default="NULL")
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    member_list = models.CharField(max_length=64, verbose_name='회원명단리스트',default=None)
    def __str__(self):
        return self.room_name

    class Meta:
        db_table = 'room'
        verbose_name = 'Room 명단'
        verbose_name_plural = 'Room 명단'

class Analytics(models.Model):
    room_name = models.CharField(max_length=128, verbose_name="방 이름", default="NULL")   
    email = models.EmailField(max_length=128, verbose_name="사용자",default="NULL")
    count =  models.IntegerField(verbose_name="사용자 수", default=0)
    rate = models.IntegerField(verbose_name="순위", default=0)
    level = models.IntegerField(verbose_name="집중도 레벨",default=0)
    app = models.IntegerField(verbose_name="앱 차단 점수",default=0)    
    person = models.IntegerField(verbose_name="자리 이탈 점수",default=0)
    time = models.IntegerField(verbose_name="학습 시간",default=0)
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'analytics'
        verbose_name = '집중도'
        verbose_name_plural = '집중도'
