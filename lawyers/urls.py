from django.urls import path
from . import views

urlpatterns = [
    path('', views.lawyer_list, name='lawyer_list'),
]
