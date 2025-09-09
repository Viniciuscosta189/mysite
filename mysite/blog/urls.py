from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList, name='post_list'),
]
