from django.urls import path 
from . import views
urlpatterns = [
    path('presenca', views.presenca, name='presenca'),
]