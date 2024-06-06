from django.http import HttpResponse
from django.shortcuts import render

data = {'movies': [
    {
        "id": "5",
        "title": "Jaws",
        "year": "1669"
    },
    {
        "id": "6",
        "title": "Tornado",
        "year": "1772"
    },
    {
        "id": "7",
        "title": "Executioner",
        "year": "1999"
    }
]}

def movies(request):
    return render(request, "movies/movies.html", data)

def home(request):
    return HttpResponse("Home Page")