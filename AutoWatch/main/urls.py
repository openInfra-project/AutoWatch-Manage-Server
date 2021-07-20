from django.urls import path
from . import views

#  기본 경로 = main/
urlpatterns = [
   path('', views.main),
   path('makeroom/',views.makeroom),
   path('enteroom/',views.enteroom),
]
