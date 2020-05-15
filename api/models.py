from django.db import models
from tastypie.resources import ModelResource, fields, ALL
from rental.models import Movie, Genre
from tastypie.authorization import Authorization


class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = "genres"
        allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
        authorization = Authorization()


# Create your models here.
class MovieResource(ModelResource):
    genre = fields.ToOneField(GenreResource, 'genre', full=True)

    class Meta:
        queryset = Movie.objects.all()
        resource_name = "movies"  # for API this will be the url api/movies
        filtering = {
            'price': ALL,
            'title': ALL,
            'release_year': ALL
        }
        ordering: ['release_year', 'price', 'title', 'director']
        allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
        authorization = Authorization()


"""
Filtering:

?price=20 Equal

?price__gt=10 Greater than
?price__lt=30 Lower Than

?title_contains=Star Wars 

"""
