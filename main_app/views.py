from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Bookmark, Tag

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def bookmarks_index(request):
    sort = request.GET.get('sort', 'id_desc')

    if sort == 'title_asc':
        bookmarks = Bookmark.objects.filter(user=request.user).order_by('title')
    elif sort == 'title_desc':
        bookmarks = Bookmark.objects.filter(user=request.user).order_by('-title')
    elif sort == 'id_asc':
        bookmarks = Bookmark.objects.filter(user=request.user).order_by('id')
    elif sort == 'id_desc':
        bookmarks = Bookmark.objects.filter(user=request.user).order_by('-id')
    return render(request, 'bookmarks/index.html', {'bookmarks': bookmarks})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'home.html')

@login_required
def bookmarks_detail(request, bookmark_id):
    bookmark = Bookmark.objects.get(id=bookmark_id)
    return render(request, 'bookmarks/detail.html', {
        'bookmark': bookmark
    })

class BookmarkCreate(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url', 'tags']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookmarkUpdate(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = '__all__'

class BookmarkDelete(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = '/bookmarks/'

class TagList(LoginRequiredMixin, ListView):
    model = Tag

class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag

class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name', 'desc']

class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = '/tags'