from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('logout/', views.logout),




    # APP
    path('app_signup', views.app_signup),
    path('app_login', views.app_login),
    path('app_image', views.app_image),
    path('app_delete', views.app_delete),
    path('app_mypage', views.app_mypage),
    path('app_modify', views.app_modify)

]
