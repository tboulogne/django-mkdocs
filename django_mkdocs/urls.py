from django.urls import path
from . import views
from django.contrib import admin

admin.autodiscover()

app_name = 'mkdocs'

urlpatterns = [
    path('path:string', views.documentation, name="mkdocs"),
]
