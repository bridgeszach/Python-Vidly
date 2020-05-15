from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Movie,Genre

# Create your views here.

# We Create functions that takes the request from the user
# and emits a response

def index(request):
    return render(request,'views/index.html')
    #return HttpResponse("Hello World")


"""
read all : Movie.objects.all()
get by id Movie.objects.get(id=1)
filter : Movie.objects.filter(in_stock=0)
"""
def catalog(request):
    movies=Movie.objects.all() #read the movies tables
    #titles=', '.join([m.title for m in movies])
    # HttpResponse(titles)
    return render(request,'views/catalogtest.html',{'title':"From BackEnd",'movies':movies})


def test(request):
    return HttpResponse("This is a test page!")

def developer(request):
    return HttpResponse("<h1>Dev: Alfredo Calderon</h1>")


def details(request,movie_id):
    try:
        movie=Movie.objects.get(id=movie_id)# read that movie
        return render(request,'views/details.html',{"id": movie_id, "movie":movie})
    except Movie.DoesNotExist:
        raise Http404()

