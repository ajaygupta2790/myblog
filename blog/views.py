from datetime import datetime, timedelta
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import Context,loader
from django.shortcuts import render_to_response
from blog import models as m
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    two_days_ago = datetime.utcnow() - timedelta(days=4)
    recent_posts = m.Post.objects.filter(created_at__gt=two_days_ago).all()
    context = Context({
        'post_list': recent_posts
    })
    return render(request, 'index.html', context)                                                                  
    
# post_detail accepts two arguments: the normal request object and an integer
# whose value is mapped by post_id defined in r'^post/(?P<post_id>\d+)/detail.html$'
def post_detail(request, post_id):
    try:
        post = m.Post.objects.get(pk=post_id)
    except m.Post.DoesNotExist:
        # If no Post has id post_id, we raise an HTTP 404 error.
        raise Http404
    return render(request, 'detail.html', {'post': post})

def post_upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html', {})
    elif request.method == 'POST':
        post = m.Post.objects.create(content=request.POST['content'],
                                     created_at=datetime.utcnow())
        # No need to call post.save() at this point -- it's already saved.
        return HttpResponseRedirect(reverse('blog.views.post_detail', kwargs={'post_id': post.id}))

def get_travel(request):
    recent_travel=m.Travel.objects.all()
    paginator = Paginator(recent_travel, 3) 
    page = request.GET.get('page')
    try:
        travel_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        travel_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        travel_list = paginator.page(paginator.num_pages)

    return render_to_response('travel.html', {"travel_list": travel_list})
    #context=Context({
      #  'travel_list':recent_travel
     #   })
    #return render(request, 'travel.html', context)

def travel_detail(request, travel_id):
    try:
        travel = m.Travel.objects.get(pk=travel_id)
    except m.Travel.DoesNotExist:
        # If no Post has id post_id, we raise an HTTP 404 error.
        raise Http404
    return render(request, 'detail1.html', {'travel': travel})