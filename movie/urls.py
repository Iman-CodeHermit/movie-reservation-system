from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('comment/', views.CreateCommentView.as_view(), name= 'comment'),
    path('movies/<int:pk>/like/', views.LikeMovieView.as_view(), name='movie-like'),
]