from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('login/', views.user_login, name='login'),
    ]
