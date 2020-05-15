from django.urls import path
from . import views

#add objects to map urls with actions in view.py

urlpatterns=[
    path('',views.index, name='index'),
    path('home',views.index, name='home'),
    path('test/test',views.test, name='test'),
    path('developer',views.developer, name='developer'),
    path('catalog',views.catalog,name='catalog'),
    path('details/<int:movie_id>', views.details, name='details')
]