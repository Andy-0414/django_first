from django.urls import path
from . import views

urlpatterns = [
    path('http/', views.http,name="http"),
]