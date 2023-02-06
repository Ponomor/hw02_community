from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group
from django.contrib.auth.decorators import login_required

 

def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    output = []
    for item in latest:
        output.append(item.text)   
    return render(request, 'index.html', {"posts":latest})
    return HttpResponse('\n'.join(output)) 

def new_post(request):
    return render(request, 'new.html')

@login_required
def group_posts(request, slug): 
    # print('request - ', request)
    # print('args - ', args)
    # print('kwargs - ', kwargs)
    # slug = kwargs['slug']
    group = get_object_or_404(Group, slug=slug) 
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:12]
    return render(request, 'group.html', {"posts":posts, "group":group }) 




