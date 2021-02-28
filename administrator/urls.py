from django.urls import path
from . import views

app_name = 'administrator'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]