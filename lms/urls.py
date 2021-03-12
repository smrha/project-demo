from django.urls import path
from . import views

app_name = 'lms'

urlpatterns = [
    path('', views.index, name='index'),
    path('term/list/', views.term_list, name='term_list'),
    path('term/new/', views.term_new, name='term_new'),
    path('term/edit/<int:pk>/', views.term_edit, name='term_edit'),
]