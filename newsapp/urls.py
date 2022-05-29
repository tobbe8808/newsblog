from django.urls import path
from . import views
from .views import post_view, like_post


app_name = 'newsapp'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path('', post_view, name='post-list'),
    path('like/', like_post, name='like-post'),
]