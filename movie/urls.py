from django.urls import path
from . import views

app_name = 'movie'
url_patterns = [
    path('comment/', views.CreateCommentView.as_view(), name= 'comment'),
]