from django.db import models

# Create your models here.
class Bookmark(models.Model):
    date_created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    url = models.TextField(max_length=250)
