from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('logout/', views.logout),
    # path('appExam/', views.appExam),
    # path('appStudy/', views.appStudy),



    # APP
    path('app_signup', views.app_signup),
    path('app_login', views.app_login),
    path('app_image', views.app_image),
    path('app_delete', views.app_delete),
    path('app_mypage', views.app_mypage),
    path('app_modify', views.app_modify),
    path('app_checkin', views.app_checkin),
    path('app_checkout', views.app_checkout),
    path('app_sendcount', views.app_sendcount)

]
