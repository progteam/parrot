"""
backend/about/urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.urls import path
from .views import progteam_desc, meeting_info, officer_info

# pylint: disable=invalid-name
urlpatterns = [
    path('meeting-info', meeting_info),
    path('officer-info', officer_info),
    path('progteam-desc', progteam_desc),
]
