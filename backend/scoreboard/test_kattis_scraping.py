"""
backend/scoreboard/test_kattis_scraping.py

Tests for Kattis Scraping Functions
"""
from django.test import TestCase
from backend.scoreboard.kattis_scraping import (
    Error404,
    ErrorInvalid,
    get_score,
    get_rank,
)


class KattisScrapingTestCase(TestCase):
    """ The Kattis Scraping utility functions
    - have no errors on a valid user handle
    - raise Error404 when the user handle does not exist
    - raise ErrorInvalid when we want the school to be CSUMB
    """
    def test_get_score(self):
        """get_score has no errors on a valid user handle
        """
        self.assertTrue(get_score('ryan-beck') > 0)

    def test_get_rank(self):
        """get_rank has no errors on a valid user handle
        """
        self.assertTrue(get_rank('ryan-beck') > 0)

    def test_fake_handle_throws_exception_404(self):
        """it raises Error404 when the user handle does not exist
        """
        with self.assertRaises(Error404):
            get_score('')
        with self.assertRaises(Error404):
            get_rank('')

    def test_non_csumb_handle_throws_exception_invalid(self):
        """it raises ErrorInvalid when we want the school to be CSUMB
        """
        with self.assertRaises(ErrorInvalid):
            get_score('xiaowuc1', check_school=True)
        with self.assertRaises(ErrorInvalid):
            get_rank('xiaowuc1', check_school=True)
