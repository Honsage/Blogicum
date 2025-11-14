from django.shortcuts import render


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def rules(request):
    context = {}
    return render(request, 'pages/rules.html', context)
