from django.contrib import admin
from .models import Room
from .models import Analytics
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display =('room_name','room_password','file','mode','maker','make_date')

admin.site.register(Room, RoomAdmin)

class AnalyticsAdmin(admin.ModelAdmin):
    list_display =('room_name','email','app','person','time','make_date')

admin.site.register(Analytics, AnalyticsAdmin)