from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()





urlpatterns = [
    # Examples:
     url(r'^', include ('qa.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
