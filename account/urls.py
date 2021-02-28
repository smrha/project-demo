from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.login, name='login'),
    path('profile', views.user_profile, name='user_profile'),
]