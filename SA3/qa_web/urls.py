from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path(r'login/', views.user_login, name='login')
]