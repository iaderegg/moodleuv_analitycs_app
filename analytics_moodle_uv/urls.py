from django.urls import path

from . import views

urlpatterns = [
  path('', views.general_summary, name='general_summary'),
  path('users', views.users_section, name='users'),
  path('get_general_summary/', views.get_general_summary, name='get_general_summary') 
]