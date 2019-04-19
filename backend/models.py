"""
backend/models.py

Site-level data models
"""
from datetime import datetime

from django.contrib import admin
from django.db import models


class AcademicTerm(models.Model):
    """Academic terms @ CSUMB
    """
    end_date = models.DateField()
    start_date = models.DateField()
    term_name = models.CharField(max_length=8)

    @staticmethod
    def current():
        """ Current academic term
        The last semester which has a start date less than today
        """
        return AcademicTerm.objects.filter(
            start_date__lte=datetime.today()
        ).order_by('start_date').last()

    def __str__(self):
        return self.term_name

# Allow admins to edit the data models
admin.site.register(AcademicTerm)
