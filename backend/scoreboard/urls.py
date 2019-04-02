"""
backend/scoreboard/urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.urls import path
from .views import scores_week

# pylint: disable=invalid-name
urlpatterns = [
    path('week', scores_week)
]
