from django.conf.urls import url
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^(?P<path>.*)$', views.documentation, name="mkdocs"),
]
