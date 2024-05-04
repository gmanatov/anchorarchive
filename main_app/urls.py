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
    path('tags/', views.TagList.as_view(), name='tags_index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/logout/', views.user_logout, name='user_logout'),
] 