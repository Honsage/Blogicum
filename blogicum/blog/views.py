from django.shortcuts import render


def index(request):
    return render(request, '', {})


def post_detail(request, id):
    return render(request, '', {})


def category_posts(request, category_slug):
    return render(request, '', {})
