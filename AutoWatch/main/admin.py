from django.contrib import admin
from .models import Room
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display =('room_name','room_password','file','mode','maker')

admin.site.register(Room, RoomAdmin)