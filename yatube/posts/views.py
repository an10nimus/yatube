from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model() 


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})


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
