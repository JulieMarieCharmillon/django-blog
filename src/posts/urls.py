from django.contrib import admin
from django.urls import path

from posts.views import BlogHome, BlogPostCreate, BlogPostDelete, BlogPostDetail, BlogPostUpdate

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create-post"),
    path('update/<str:slug>/', BlogPostUpdate.as_view(), name="update-post"),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name="delete-post"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="post"),
    
]
