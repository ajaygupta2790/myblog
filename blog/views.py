from datetime import datetime, timedelta
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import Context
from blog import models as m
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
    
def index(request):
    two_days_ago = datetime.utcnow() - timedelta(days=2)
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