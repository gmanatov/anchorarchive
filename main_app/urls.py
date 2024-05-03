from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bookmarks/', views.bookmarks_index, name='index'),
    path('bookmarks/<int:bookmark_id>/', views.bookmarks_detail, name='detail'),
    path('bookmarks/create/', views.BookmarkCreate.as_view(), name='bookmarks_create'),
    path('bookmarks/<int:pk>/update/', views.BookmarkUpdate.as_view(), name='bookmarks_update'),
    path('bookmarks/<int:pk>/delete/', views.BookmarkDelete.as_view(), name='bookmarks_delete'),
] 