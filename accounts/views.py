
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def signup(request):
    """User signup view."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Create the new user
            return redirect('login')  # Redirect to login page after successful signup
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
            login(request, user)              # Log the user in (persist session)
            return redirect('home')           # Go to the homepage
        else:
            # Invalid credentials, re-render the page with an error
            return render(request, 'login.html', {
                'error': "Invalid username or password."
            })
    # GET request or failed login:
    return render(request, 'login.html')

@login_required
def home(request):
    """Home page (dashboard) - only accessible to logged-in users."""
    return render(request, 'home.html')

def logout_view(request):
    """Log the user out and redirect to login page."""
    logout(request)
    return redirect('login')
