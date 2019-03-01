from django.test import TestCase
import backend.scoreboard.kattis_scraping as kattis_scraping


class KattisScrapeTestCase(TestCase):
    def setUp(self):
        pass

    def test_get_points_throws_exception_404(self):
        with self.assertRaises(kattis_scraping.Error404):
            kattis_scraping.get_points("")

    def test_get_points_not_throws_exception_404(self):
        try:
            kattis_scraping.get_points("ryan-beck")
        except kattis_scraping.Error404:
            self.fail()

    def test_get_points_throws_exception_invalid(self):
        with self.assertRaises(kattis_scraping.ErrorInvalid):
            kattis_scraping.get_points("xiaowuc1")

    def test_get_points_not_throws_exception_invalid(self):
        try:
            kattis_scraping.get_points("ryan-beck")
        except kattis_scraping.ErrorInvalid:
            self.fail()

    def test_get_rank_throws_exception_404(self):
        with self.assertRaises(kattis_scraping.Error404):
            kattis_scraping.get_rank("")

    def test_get_rank_not_throws_exception_404(self):
        try:
            kattis_scraping.get_rank("ryan-beck")
        except kattis_scraping.Error404:
            self.fail()

    def test_get_rank_throws_exception_invalid(self):
        with self.assertRaises(kattis_scraping.ErrorInvalid):
            kattis_scraping.get_rank("xiaowuc1")

    def test_get_rank_not_throws_exception_invalid(self):
        try:
            kattis_scraping.get_rank("ryan-beck")
        except kattis_scraping.ErrorInvalid:
            self.fail()
