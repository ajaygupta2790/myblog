from django.conf.urls import patterns, include, url
from blog import views
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',                                                   
    #url(r'^$','blog.views.index', name='index'),
    # Map the view function myblog.views.post_detail() to an URL pattern
    #url(r'^post/(?P<post_id>\d+)/detail.html$',
        #'blog.views.post_detail', name='post_detail'),
    url(r'^blog/', include('blog.urls')),                          
    # Uncomment the next line to enable the admin:
    # (r'^accounts/', include('registration.backends.default.urls')),  
    # (r'^accounts/', include('registration.urls')),                         
    url(r'^admin/', include(admin.site.urls)),                               
)