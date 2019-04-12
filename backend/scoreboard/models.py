"""
backend/scoreboard/models.py

Scoreboard data models
"""
from django.contrib import admin
from django.db import models


class KattisHandle(models.Model):
    """Kattis handle can be subscribed or unsubscribed
    - it has many Kattis scores
    - TODO: it (may) belongs to a user
    """
    handle = models.CharField(max_length=50)
    subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_score(self, score):
        """Add a score snapshot for the current Kattis handle
        To actually perform the query, save() needs to be called. Read more at
            https://docs.djangoproject.com/en/2.1/ref/models/querysets/
        We do not execute a query every when this function is called, or it
        will be too slow (when there're many add_score calls). Instead, we
        should create the objects in memory, and use bulk-create:
            https://docs.djangoproject.com/en/2.1/ref/models/querysets/#bulk-create
        """
        return KattisScore(kattis_handle=self, score=score)

    def scores(self):
        """Return all the score snapshots for the current kattis handle
        """
        return KattisScore.objects.filter(kattis_handle=self)

    def __str__(self):
        return '%s' % self.handle


class KattisScore(models.Model):
    """ A Kattis score snapshot, obtained by scrapping Kattis Website
    - it belongs to a Kattis handle
    - it shall not be modified once created
    """
    kattis_handle = models.ForeignKey(KattisHandle, on_delete=models.CASCADE)
    score = models.FloatField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[%s] %s: %s' % (self.created_at, self.kattis_handle, self.score)

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]


# Allow admins to add KattisHandle
admin.site.register(KattisHandle)
