from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bookmark, Tag

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bookmarks_index(request):
    sort = request.GET.get('sort', 'id_desc')

    if sort == 'title_asc':
        bookmarks = Bookmark.objects.all().order_by('title')
    elif sort == 'title_desc':
        bookmarks = Bookmark.objects.all().order_by('-title')
    elif sort == 'id_asc':
        bookmarks = Bookmark.objects.all().order_by('id')
    elif sort == 'id_desc':
        bookmarks = Bookmark.objects.all().order_by('-id')
    return render(request, 'bookmarks/index.html', {'bookmarks': bookmarks})

def bookmarks_detail(request, bookmark_id):
    bookmark = Bookmark.objects.get(id=bookmark_id)
    return render(request, 'bookmarks/detail.html', {
        'bookmark': bookmark
    })

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = '__all__'

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = '__all__'

class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = '/bookmarks/'

class TagList(ListView):
    model = Tag

class TagDetail(DetailView):
  model = Tag

class TagCreate(CreateView):
  model = Tag
  fields = '__all__'

class TagUpdate(UpdateView):
  model = Tag
  fields = ['name', 'desc']

class TagDelete(DeleteView):
  model = Tag
  success_url = '/tags'