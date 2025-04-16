from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Movie

def signup(request):
    """User signup view."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    """User login view."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('movie_list')  # Redirect to the home page after login
        else:
            return render(request, 'login.html', {
                'error': "Invalid username or password."
            })
    return render(request, 'login.html')



def home(request):
    """Home page (dashboard) - only accessible to logged-in users."""
    return render(request, 'home.html')


def logout_view(request):
    """Log the user out and redirect to login page."""
    logout(request)
    return redirect('login')


def movie_list(request):
    """View for displaying the list of movies."""
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    """View for displaying movie details."""
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})
