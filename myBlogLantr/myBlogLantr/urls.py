from django.conf.urls import patterns, include, url
from django.contrib import admin
from myblogCore.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlogLantr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', index, name = 'index'),
)
