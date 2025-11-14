from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    context = {}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    context = {}
    return render(request, 'blog/category.html', context)
