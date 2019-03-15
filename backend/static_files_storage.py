"""
backend/retrieve_index_file.py

StaticFilesStorage. Extend StaticFilesStorage to add post_process hook.
"""
import os

from django.contrib.staticfiles import storage
from .retrieve_index_file import retrieve_index_file, DST


class StaticFilesStorage(storage.StaticFilesStorage):
    """Extend StaticFilesStorage to add post_process hook. The collectstatic
    management command calls the post_process() method of the
    STATICFILES_STORAGE after each run and passes a list of paths that have
    been found by the management command.
    """
    # pylint: disable=no-self-use,unused-argument
    def post_process(self, *args, **kwargs):
        """Retrieve index file after collecting static files
        Read more at
            https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.StaticFilesStorage.post_process
        """
        retrieve_index_file(debug=False)
        # [(original_path: string, processed_path: string, processed: boolean)]
        return [('', '', os.path.exists(DST))]
