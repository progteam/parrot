import json
from django.test import TestCase

class AboutPageViewTests(TestCase):
    fixtures = [
        'meetinginfo.json',
        'officerinfo.json',
        'progteamdesc.json',
    ]

    def test_meeting_info(self):
        """Test route /about/meeting-info
        - it returns status code 200
        - it returns a non-empty list
        """
        response = self.client.get('/about/meeting-info')
        self.assertEqual(response.status_code, 200)

        obj = json.loads(response.content)
        self.assertTrue(isinstance(obj, list))
        self.assertTrue(len(obj) > 0)

    def test_officer_info(self):
        """Test route /about/officer-info
        - it returns status code 200
        - it returns a non-empty list
        """
        response = self.client.get('/about/officer-info')
        self.assertEqual(response.status_code, 200)

        obj = json.loads(response.content)
        self.assertTrue(isinstance(obj, list))
        self.assertTrue(len(obj) > 0)

    def test_progteam_desc(self):
        """Test route /about/progteam-desc
        - it returns status code 200
        - it has a non-empty description
        """
        response = self.client.get('/about/progteam-desc')
        self.assertEqual(response.status_code, 200)

        obj = json.loads(response.content)
        self.assertTrue('desc' in obj)
        self.assertTrue(len(obj['desc']) > 0)
