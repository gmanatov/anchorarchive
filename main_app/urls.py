from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bookmarks/', views.bookmarks_index, name='index'),
    path('bookmarks/<int:bookmark_id>/', views.bookmarks_detail, name='detail'),
] 