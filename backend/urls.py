"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path

from .views import error404, index, serve_dev_assets


# pylint: disable=invalid-name
urlpatterns = [
    path('', index),
    path('about/', include('backend.about.urls')),
    path('events/', include('backend.events.urls')),
    path('admin/', admin.site.urls),

    path('scoreboard/', include('backend.scoreboard.urls')),
]

# Set our 404 error handler. Read more at
#   https://docs.djangoproject.com/en/2.1/ref/views/#error-views
handler404 = error404

if settings.DEBUG:
    # Since we use Django to serve the static assets during development, we add
    # a fallback view to handle these requests. Note pattern /.*/ matches any
    # URLs; thus it has to be added at the end of the URL patterns list.
    urlpatterns.append(re_path(r'.*', serve_dev_assets))
