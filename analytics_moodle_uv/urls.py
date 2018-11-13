from django.urls import path
from . import views

urlpatterns = [
  path('', views.general_summary, name='general_summary'),
]