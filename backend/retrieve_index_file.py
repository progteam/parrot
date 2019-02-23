"""
backend/retrieve_index_file.py

Retrive the index file from the frontend build dir in dev, or from CDN in prod.
"""
import os
import urllib.request

from django.conf import settings


INDEX = 'index.html'
DST = f"{settings.BACKEND_TEMPLATES_DIR}/{INDEX}"


def retrieve_index_file(debug=settings.DEBUG):
    """ Retrive the index file. It needs to be called before the server starts.
    """
    if debug:
        # Remove the index file if exists so we can create the symlink
        if os.path.exists(DST):
            os.remove(DST)
        # We only need to create the link if the link does not exist
        if not os.path.islink(DST):
            os.symlink(f"{settings.FRONTEND_BUILD_DIR}/{INDEX}", DST)
    else:
        # Remove the symlink if exists. Otherwise, the retrieved index file would
        # overwrite the index file in the frontend build directory.
        if os.path.islink(DST):
            os.remove(DST)
        # Retrive the index file from the CDN in production
        urllib.request.urlretrieve(
            f"{os.environ['PARROT_CDN_HOST']}/{INDEX}", DST)
