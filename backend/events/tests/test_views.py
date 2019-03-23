"""
backend/events/tests/test_views.py

Tests for the events page views. We use the test client. Read more at
    https://docs.djangoproject.com/en/2.1/topics/testing/tools/
"""
import json
from django.test import TestCase

class EventsPageViewTests(TestCase):
    """Events page view tests for route /events/data
    """
    fixtures = [
        'event.json',
        'team.json',
        'teammember.json',
    ]

    def test_events_data(self):
        """Test route /events/data
        - it returns status code 200
        - it returns a non-empty list
        """
        response = self.client.get('/events/data')
        self.assertEqual(response.status_code, 200)

        obj = json.loads(response.content)
        self.assertTrue(isinstance(obj, list))
        self.assertTrue(len(obj) > 0)
