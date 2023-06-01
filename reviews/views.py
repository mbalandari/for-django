from django.shortcuts import render


def index(request):
    name = "Maz"
    return render(request, "base.html", {"name": name})
