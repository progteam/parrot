"""
backend/events/urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.urls import path
from .views import events_data

# pylint: disable=invalid-name
urlpatterns = [
    path('data', events_data),
]
