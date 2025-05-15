from chatbot import views
from django.urls import path

urlpatterns = [
    path('chat/', views.chat, name='chat')
]