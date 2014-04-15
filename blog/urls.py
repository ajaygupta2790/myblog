from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/detail.html$', views.post_detail, name='detail'),
    url(r'^post/upload.html$', views.post_upload, name='post_upload'),
    # ex: /polls/5/results/
)
