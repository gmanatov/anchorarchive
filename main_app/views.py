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

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = '__all__'

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ('title', 'url')

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











# TODO Temporary DUMMY Database - REMOVE THIS AFTER ADDING BOOKMARK MODEL
# bookmarks = [
#     {'id': '3150',
#      'date_created': '04/23/2024', 
#      'title' : 'CSS Anchor Is The Best New CSS Feature Since Flexbox', 
#      'url' : 'https://www.youtube.com/shorts/fO0XD75u2TI'},
#     {'id': '2677',
#      'date_created': '05/02/2024', 
#      'title' : 'Google apprenticeships for 2024 US', 
#      'url' : 'https://www.reddit.com/r/google/comments/18b4tr2/google_apprenticeships_for_2024_us/'},
#     {'id': '8142',
#      'date_created': '04/29/2024', 
#      'title' : 'IBM Apprenticeships', 
#      'url' : 'https://www.ibm.com/careers/search?q=apprentice'},
#     {'id': '4721',
#      'date_created': '05/02/2024', 
#      'title' : 'USA Google Software Apprenticeships', 
#      'url' : 'https://www.google.com/about/careers/applications/jobs/results/?distance=50&hl=en_US&jlo=en_US&location=United%20States&q=%22Software%20Engineering%20(SWE)%20Apprenticeship%22&src=Online%2FGoogle%20Website%2FByF&utm_campaign=&utm_medium=information_technology_apprenticeship_us&utm_source=byf'},
# ]
