from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<str:roomid>/', views.room, name= 'room'),
    path('checkroom', views.checkroom, name= 'checkroom'),
    path('send', views.send, name= 'send'),
    path('messages/<str:roomid>/', views.messages, name= 'messages'),
]
