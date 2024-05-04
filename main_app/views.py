from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bookmark, Tag

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bookmarks_index(request):
    bookmarks = Bookmark.objects.all().order_by('-id')
    return render(request, 'bookmarks/index.html', {
        'bookmarks': bookmarks
    })

def bookmarks_detail(request, bookmark_id):
    bookmark = Bookmark.objects.get(id=bookmark_id)
    return render(request, 'bookmarks/detail.html', {
        'bookmark': bookmark
    })

def assoc_tag(request, bookmark_id, tag_id):
  Bookmark.objects.get(id=bookmark_id).tags.add(tag_id)
  return redirect('detail', bookmark_id=bookmark_id)

def unassoc_tag(request, bookmark_id, tag_id):
  Bookmark.objects.get(id=bookmark_id).tags.remove(tag_id)
  return redirect('detail', bookmark_id=bookmark_id)

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