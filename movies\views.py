from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Country, Genre, Language
from .forms import MovieForm
from django.db.models import Q
import matplotlib.pyplot as plt
import io, base64

def index(request):
    return redirect('movies:list')

def movie_list(request):
    movies = Movie.objects.all().order_by('-rating')
    return render(request, 'movies/list.html', {'movies': movies})

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            country = request.POST.get('country')
            genre = request.POST.get('genre')
            lang = request.POST.get('lang')
            if country:
                Country.objects.create(movie=movie, name=country)
            if genre:
                Genre.objects.create(movie=movie, name=genre)
            if lang:
                Language.objects.create(movie=movie, name=lang)
            return redirect('movies:list')
    else:
        form = MovieForm()
    return render(request, 'movies/add.html', {'form': form})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:list')
    return render(request, 'movies/delete.html', {'movie': movie})

def movie_search(request):
    q = request.GET.get('q', '')
    movies = Movie.objects.filter(Q(name__icontains=q))
    return render(request, 'movies/list.html', {'movies': movies, 'q': q})

def movie_filter(request):
    country = request.GET.get('country')
    genre = request.GET.get('genre')
    rating_min = request.GET.get('rating_min')
    rating_max = request.GET.get('rating_max')

    qs = Movie.objects.all()
    if country:
        qs = qs.filter(countries__name=country)
    if genre:
        qs = qs.filter(genres__name=genre)
    if rating_min and rating_max:
        qs = qs.filter(rating__gte=float(rating_min), rating__lte=float(rating_max))

    return render(request, 'movies/list.html', {'movies': qs})

def ratings_graph(request):
    movies = Movie.objects.all().order_by('name')
    names = [m.name for m in movies]
    ratings = [m.rating for m in movies]
    plt.figure(figsize=(10,5))
    plt.plot(names, ratings, marker='o')
    plt.xticks(rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    image_png = buf.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buf.close()
    return render(request, 'movies/graph.html', {'graph': graph})
