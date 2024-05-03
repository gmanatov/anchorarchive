from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    date_created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    url = models.TextField(max_length=250)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bookmark_id': self.id})
    