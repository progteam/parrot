"""
backend/about/models.py

About page data models
- ProgteamDesc
    - Brief history and the missions/objectives of progteam
- MeetingInfo
    - The meeting time/locations
- OfficerInfo
    - The officers and their contact information
"""
from django.contrib import admin
from django.db import models


class ProgteamDesc(models.Model):
    """Progteam Description

    This model contains a text description, which is rendered on the frontend
    about page. We allow html content in the text filed.
    """
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.desc


class MeetingInfo(models.Model):
    """Meeting information

    This model stores meeting time and locations. Note the time-related fields
    need to be entered as the 24-hours format.
    """
    day_of_week = models.CharField(
        max_length=50,
        # choices: Monday - Friday
        choices=(
            ('monday', 'Monday'),
            ('tuesday', 'Tuesday'),
            ('wednesday', 'Wednesday'),
            ('thursday', 'Thursday'),
            ('friday', 'Friday')))
    room = models.CharField(max_length=50)
    term = models.CharField(max_length=32)
    time_end = models.TimeField()
    time_start = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[%s] %s %s - %s %s '% (
            self.term,
            self.day_of_week,
            self.time_start,
            self.time_end,
            self.room,
        )


class OfficerInfo(models.Model):
    """The contact information of an officer
    """
    email = models.EmailField()
    name = models.CharField(max_length=256)
    profile_img = models.URLField()
    role = models.CharField(max_length=50)
    term = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[%s %s] %s <%s>' % (
            self.role,
            self.term,
            self.name,
            self.email,
        )


# Allow admins to edit the data models
admin.site.register(ProgteamDesc)
admin.site.register(MeetingInfo)
admin.site.register(OfficerInfo)
