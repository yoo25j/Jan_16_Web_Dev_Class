from django.conf.urls import include, url
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    url(r'^$', list_views.home_page, name = 'home'),
    url(r'^list/', include(list_urls)),
]
