"""
backend/scoreboard/management/commands/prunekattisscore.py

The prunekattisscore command for pruning the KattisScore table
"""
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.utils.timezone import get_current_timezone

from backend.scoreboard.models import KattisHandle, KattisScore

class Command(BaseCommand):
    """Command prunekattisscore

    We run the scraping tool regularly to make sure the scoreboard page could
    have relatively low latency. We would not store all the score snapshots for
    all subscribed handles. Thus we use this command to prune the KattisScore
    table and make sure it has a maintainable size. Read more:
        https://github.com/progteam/parrot/issues/36
    """
    def add_arguments(self, parser):
        """Add command line arguments

        This allows us to control the selectivity between the breakpoints.
        Read more at
            https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/#django.core.management.BaseCommand.add_arguments
        """
        parser.add_argument(
            '-s',
            default=[72, 36, 18],
            dest='selectivity',
            help="""
            set the selectivity for the 3 breakpoints (24h - 7d - 4w - 24w
            ago). For each selectivity value s, we will keep at most (2 * s)
            data points.
            """,
            nargs=3,
            type=int,
        )

    def handle(self, *args, **options):
        kattis_handles = KattisHandle.objects.all()
        # Calculate the breakpoints
        now = datetime.now(tz=get_current_timezone())
        breakpoints = [
            now - timedelta(hours=24),
            now - timedelta(days=7),
            now - timedelta(weeks=4),
            now - timedelta(weeks=24),
        ]
        # Get the arguments from the parser
        sel = options['selectivity']
        for kattis_handle in kattis_handles:
            # For each kattis handle, prune the data points between the
            # breakpoints
            for i in range(1, len(breakpoints)):
                scores = KattisScore.objects.filter(
                    kattis_handle=kattis_handle,
                    created_at__range=(
                        breakpoints[i],
                        breakpoints[i - 1],
                    ),
                ).order_by('score')
                step_size = len(scores) // sel[i - 1]
                if step_size <= 1:
                    continue
                for j, score in enumerate(scores):
                    if j % step_size != 0:
                        score.delete()
            # Delete all the data points after the last breakpoint
            KattisScore.objects.filter(
                kattis_handle=kattis_handle,
                created_at__date__lt=breakpoints[-1],
            ).delete()
