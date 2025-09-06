from django.urls import path
from . import views

urlpatterns=[
    path('', views.landing, name="Landing page"),
    path('chat/', views.chat, name="Chat"),
]