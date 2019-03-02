"""
backend/test_redirect_404.py

Redirect 404 Tests. If we failed to find a static file and none of the URLs
matched, instead of raising a 404 error, we serve the index file and let the
frontend to render the 404 page.

See also:
- backend/urls.py
- backend/views.py
"""
from django.test import TestCase
from django.http.response import HttpResponseRedirect

class Redirect404Tests(TestCase):
    """ Redirect 404 Tests
    - it redirects invalid pages to the index page
    - it matches URL before redirecting the 404 page to the index page
    """
    def test_redirect(self):
        """When visit a fake page, the client is redirected to the index page
        - both index and fake_page have status code 200
        - they have the exact same content
        """
        response_index = self.client.get('/')
        self.assertEqual(response_index.status_code, 200)

        response_fake_page = self.client.get('/fake-page')
        self.assertEqual(response_fake_page.status_code, 200)

        self.assertEqual(
            list(response_index.content)[0],
            list(response_fake_page.content)[0])

    def test_matching_url(self):
        """When visit /admin/, the client is redirected to the admin login
        - Client is rediected to the Django adnmin page
            /admin/login/?next=/admin/
        - We shall get an HttpResponseRedirect response
        """
        response = self.client.get('/admin/')
        self.assertTrue(isinstance(response, HttpResponseRedirect))
