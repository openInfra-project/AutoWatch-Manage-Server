from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=64, verbose_name="방 이름")
    room_password = models.CharField(max_length=64, verbose_name="방 비밀번호")
    file = models.FileField(verbose_name="파일")

    def __str__(self):
        return self.room_name

    class Meta:
        db_table = 'room'
        verbose_name = 'Room 명단'
        verbose_name_plural = 'Room 명단'