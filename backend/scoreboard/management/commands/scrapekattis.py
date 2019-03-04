"""
backend/scoreboard/management/commands/scrapekattis.py

This is a command for scraping user scores from Kattis. The command is
regularly called by the scheduler to save score snapshots for each subscribed
user. Read more at
    https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/
"""
from django.core.management.base import BaseCommand

from backend.scoreboard.kattis_scraping import get_points
from backend.scoreboard.models import KattisHandle, KattisScore


class Command(BaseCommand):
    """Command scrapekattis

    This command will be run regularly by the Heroku Scheduler. It scrapes the
    user score and ranking information and stores them into the database.
    """
    def handle(self, *args, **options):
        kattis_handles = KattisHandle.objects.filter(subscribed=True)
        scores = []
        for handle in kattis_handles:
            try:
                scores.append(handle.add_score(get_points(handle)))
            except Exception as e:
                print('error: failed to load handle %s' % (handle))
        KattisScore.objects.bulk_create(scores)
