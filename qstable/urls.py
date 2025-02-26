from django.urls import path
from . import views


urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),

]