from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator


User = get_user_model() 


def index(request):
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator}
    )


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'group.html',
        {'group': group, 'page': page}
    )


@login_required
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.save()
            return redirect('index')
        return render(request, 'new_post.html', {'form': form})
    form = NewPostForm()
    return render(request, 'new_post.html', {'form': form})

def profile(request):
    user = User.objects.all()

    return render(request, 'profile.html', {})

def post_view(request):
    return render(request, 'post.html', {})

