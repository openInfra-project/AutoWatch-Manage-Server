from django.urls import path
from main.views import AnalyticsList, RoomList
from . import views

#  기본 경로 = main/
urlpatterns = [
    path('', views.main),
    path('makeroom/', views.makeroom),
    path('enteroom/', views.enteroom),
    path('makeroom/success', views.make_success),
    path('enteroom/exam1',views.exam1),
    path('enteroom/exam2',views.exam2, name='exam2'),
    path('enteroom/exam3',views.exam3),
    path('enteroom/study1',views.study1),
    path('enteroom/study2',views.study2),
    path('list/',views.mylist),
    path('list/room', RoomList.as_view()),
    path('list/analytics',AnalyticsList.as_view()),
    path('list/analytics/<int:pk>',views.analyticsDetail),
    path('roomout/<int:time>/<str:mode>',views.roomout),
    path('roomout/exam',views.roomoutExam),
    path('roomout/study',views.analytics),
    path('saveImages/',views.saveImages),
    path('app_makeroom', views.app_makeroom),
    path('app_makemyroom', views.app_makemyroom),
    path('app_enter_room', views.app_enterroom),
    path('app_enter_myroom', views.app_entermyroom),
    path('app_myroom', views.app_myroom),
    path('app_images', views.app_images),
    path('app_check_myinfo', views.app_checkmyinfo),
]