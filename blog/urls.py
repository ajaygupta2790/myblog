from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/detail.html$', views.post_detail, name='detail'),
    url(r'^post/upload.html$', views.post_upload, name='post_upload'),
    url(r'^travel/travel.html$', views.get_travel, name='get_travel'),
    url(r'^travel/(?P<travel_id>\d+)/detail1.html$', views.travel_detail, name='travel_detail'),
    # ex: /polls/5/results/
)
