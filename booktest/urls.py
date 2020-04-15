from django.conf.urls import include, url
from django.contrib import admin
from booktest import views

urlpatterns = [
    url(r'^$',views.index),

    url(r'^(\d+)$',views.detail),

    url(r'^list$',views.index2),

    url(r'^create$',views.create),

    url(r'^delete(\d+)$',views.delete)
]
