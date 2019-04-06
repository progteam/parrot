"""
backend/scoreboard/test/test_command_prunekattisscore.py

Tests for the prunekattisscore command. Read more at
    https://docs.djangoproject.com/en/2.1/ref/django-admin/#django.core.management.call_command
"""
from datetime import datetime, timedelta
from unittest.mock import patch, Mock

from django.core.management import call_command
from django.test import TestCase
from django.utils.timezone import get_current_timezone

from backend.scoreboard.models import KattisScore, KattisHandle


def create_scores(num_scores, now, delta=timedelta(minutes=1)):
    """Create fake score snapshots to prune

    Use an n^2 distribution on the timeline to simulate the real table. Since
    the created_at timestamp is created automatically by Django, we mock the
    time utility method to modify the created time for testing purposes.
    """
    handle = KattisHandle.objects.create(handle='test-handle')
    for i in range(num_scores):
        created_at = str(now - delta * i * i)
        with patch('django.utils.timezone.now', Mock(return_value=created_at)):
            handle.add_score(6000 - i).save()


class PruneKattisScoreTests(TestCase):
    """Tests for the prunekattisscore command in
        backend/scoreboard/management/commands/prunekattisscore.py
    """
    def test_pruning(self):
        """Test the prunekattisscore command
        - it prunes the table and keeps x data points where x in
            [(sum(sel), 2 * sum(sel))]
        - it deletes data older than 25 weeks
        - it has no side effects if running it regularly
        """
        num_scores = 5000
        now = datetime.now(tz=get_current_timezone())
        create_scores(num_scores, now)

        objs = KattisScore.objects.all()
        self.assertEqual(len(objs), num_scores)

        sel = [72, 36, 18]
        call_command('prunekattisscore', selectivity=sel)

        pruned_size = len(KattisScore.objects.all())
        # The size of the pruned table is in the range of
        #   [(sum(sel), 2 * sum(sel))
        self.assertTrue(sum(sel) <= pruned_size < 2 * sum(sel))
        # Scores which are older than 25 weeks are deleted completely
        self.assertTrue(
            KattisScore.objects.last().created_at >= now - timedelta(weeks=25)
        )

        # Running the command consecutively would not affect the table
        call_command('prunekattisscore', selectivity=sel)
        self.assertEqual(pruned_size, len(KattisScore.objects.all()))
