from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
