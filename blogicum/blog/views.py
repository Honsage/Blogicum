from django.shortcuts import render
from django.http import Http404


def index(request):
    context = {'posts': reversed(posts.values())}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    if id not in posts.keys():
        raise Http404(f"Введен некорректный идентификатор поста: {id}")
    context = {'post': posts[id]}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    context = {'category': category_slug}
    return render(request, 'blog/category.html', context)
