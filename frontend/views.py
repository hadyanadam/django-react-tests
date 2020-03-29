from django.shortcuts import render


def index(request):
    context = {
        "konten":"coba kalo bisa ya"
    }
    return render(request, 'frontend/index.html', context)