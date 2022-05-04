from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import get_object_or_404


def index(request):
    COUNT_POSTS = 10
    posts = Post.objects.order_by('-pub_date')[:COUNT_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    COUNT_POSTS = 10
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by(
        '-pub_date')[:COUNT_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
