from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('comment/', views.CreateCommentView.as_view(), name= 'comment'),
]