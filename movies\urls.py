from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='list'),
    path('add/', views.movie_add, name='add'),
    path('delete/<int:pk>/', views.movie_delete, name='delete'),
    path('search/', views.movie_search, name='search'),
    path('filter/', views.movie_filter, name='filter'),
    path('graph/', views.ratings_graph, name='graph'),
]
