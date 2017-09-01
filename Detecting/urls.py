from django.conf.urls import include, url
import subprocess2
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls import include, url
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'Detecting.views.home', name='home'),
    # url(r'^Detecting/', include('Detecting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('SystemApp.urls')),
]
