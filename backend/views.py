from django.contrib.staticfiles.views import serve


def serve_dev_assets(request):
    """Serving compiled JS assets during development

    During development, Django collects the static files so we can serve them
    via this view.
    """
    if request.path == '/':
        return serve(request, 'index.html')
    return serve(request, request.path)
