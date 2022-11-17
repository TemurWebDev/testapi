from django.urls import path
from .views import webbook

urlpatterns = [
    path('',webbook)
]