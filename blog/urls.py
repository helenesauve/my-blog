from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('post/<slug:slug>/', BlogDetailView.as_view(), 
        name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]