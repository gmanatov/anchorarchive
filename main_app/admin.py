from django.contrib import admin
from .models import Bookmark, Tag

admin.site.register([Bookmark, Tag])
