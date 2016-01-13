
# from django.conf.urls import url
# from django.contrib import admin
from django.conf.urls import include, url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name = 'new_list'),
    url(r'^(\d+)/$', views.view_list, name = "view_list"),
    url(r'^(\d+)/items/$', views.edit_list, name = "edit_list"),
]
