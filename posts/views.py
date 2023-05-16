from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group
from django.contrib.auth.decorators import login_required
from posts.forms import NewForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
# from users.forms import CreationForm, User
from django.contrib.auth.models import User


def index(request):
        post_list = Post.objects.order_by('-pub_date').all()
        paginator = Paginator(post_list, 10)  # показывать по 10 записей на странице.
        page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
        page = paginator.get_page(page_number)  # получить записи с нужным смещением
        return render(
            request,
            'index.html',
            {'page': page, 'paginator': paginator}
       )


def new_post(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'new.html', {'form': form})
    form = NewForm()
    return render(request, 'new.html', {'form': form})

# @login_required
def profile(request, username):
    user = get_object_or_404(User, username=username) 
    posts_user = Post.objects.filter(author=user).order_by('-pub_date').all()
    # post_count = user.posts.all().count()
    post_count = Post.objects.filter(author=user).count()
    paginator = Paginator(posts_user, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'profile.html',  {'profile': user,'post_count': post_count, 'page': page, 'paginator': paginator})
 

def post_view(request, username, post_id):
    print("username-",username)
    print("post_id-",post_id)
    user = get_object_or_404(User, username=username) 
    post_views = get_object_or_404(Post, pk=post_id, author=user) #post
    post_count = Post.objects.filter(author=user).count() 


    return render(request, 'post.html', {'post_view': user,'post_views' : post_views,'post_count': post_count})

@login_required
def post_edit(request, username, post_id):
    print('Редактирую')
    user = get_object_or_404(User, username=username) 
    post_views = get_object_or_404(Post, pk=post_id, author=user) #post 
    # post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET': #False
        if request.user is not post_views.author:
            return redirect('post', post_id=post_views.pk, username=post_views.author.username)
        form = NewForm(instance=post_views)

    if request.method == 'POST': #True
        form = NewForm(request.POST, instance=post_views)
        if form.is_valid():
            form.save()
        return redirect('post_views', post_id=post_views.pk)
    return render(request, 'new.html', {'form': form,'post_views' : post_views})

@login_required
def group_posts(request, slug): 
    group = get_object_or_404(Group, slug=slug) 
    posts_list = Post.objects.filter(group=group).order_by('-pub_date').all()
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'group.html', {'page': page, 'paginator': paginator}) 




