from django.urls import path
from . import views

#  기본 경로 = main/
urlpatterns = [
    path('', views.main),
    path('makeroom/', views.makeroom),
    path('enteroom/', views.enteroom),
    path('makeroom/success', views.make_success),
    path('enteroom/exam1',views.exam1),


    path('app_makeroom', views.app_makeroom),
    path('app_makemyroom', views.app_makemyroom),
    path('app_enter_room', views.app_enterroom),
    path('app_enter_myroom', views.app_entermyroom),
    path('app_myroom', views.app_myroom),
    path('app_images', views.app_images),
    path('app_check_myinfo', views.app_checkmyinfo),
]