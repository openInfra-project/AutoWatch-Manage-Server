from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=128, verbose_name="방 이름")
    room_password = models.CharField(max_length=64, verbose_name="방 비밀번호")
    file = models.FileField(verbose_name="파일",default="NULL")
    mode = models.CharField(max_length=64, verbose_name="모드", default="NULL")
    maker = models.EmailField(max_length=64, verbose_name="생성자" , default="NULL")

    def __str__(self):
        return self.room_name

    class Meta:
        db_table = 'room'
        verbose_name = 'Room 명단'
        verbose_name_plural = 'Room 명단'