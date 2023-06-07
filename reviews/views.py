from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def welcome_view(request):
    message = f"<html><h1>Welcome to Bookr Maz!</h1><p>{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(message)


def index(request):
    return render(request, "base.html")


def search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search_result.html", {"search_text": search_text})
