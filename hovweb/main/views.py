from django.shortcuts import render


def index(request):
    data = {
        "title": "Главная страница",
        "hev": ["aaa", "ddd", "ccc"],
    }
    return render(request, "main/index.html", data)
