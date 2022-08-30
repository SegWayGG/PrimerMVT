from django.contrib import admin
from django.urls import path
from AppCoder.views import familia


urlpatterns = [
    path("familia/", familia),
]
