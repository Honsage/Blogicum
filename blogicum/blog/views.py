from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from django.db.models import Q
from .models import Category, Location, Post


def index(request):
    posts = Post.objects.select_related('category')\
                        .filter(pub_date__lte=timezone.now())\
                        .filter(is_published=True)\
                        .filter(category__is_published=True)\
                        .order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        Q(pk=id) &
        Q(pub_date__lte=timezone.now()) &
        Q(is_published=True) &
        Q(category__is_published=True)
    )

    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.select_related('category')\
                        .filter(category__slug=category_slug)\
                        .filter(pub_date__lte=timezone.now())\
                        .filter(is_published=True)\
                        .order_by('-pub_date')
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, 'blog/category.html', context)
