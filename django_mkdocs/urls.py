from django.urls import path, re_path
from django_mkdocs import views
from django.contrib import admin

admin.autodiscover()

app_name = 'mkdocs'

urlpatterns = [
    re_path(r'^(?P<path>.*)$', views.documentation, name="mkdocs"),
]
