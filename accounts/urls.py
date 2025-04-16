from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Show home page after login
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),  # Added login URL
    path('logout/', views.logout_view, name='logout'),
    path('movies/', views.movie_list, name='movie_list'),  # Correct URL for movie list
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
