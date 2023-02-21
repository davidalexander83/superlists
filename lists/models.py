from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class List(models.Model):
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank = True, null = True, on_delete = models.CASCADE)
  
  def get_absolute_url(self):
      return reverse('view_list', args = [self.id])
  

class Item(models.Model):
  text = models.TextField(default = '')
  list = models.ForeignKey(List, on_delete = models.CASCADE, default = None)

  class Meta:
    unique_together = ('list', 'text')

  def __str__(self):
    return self.text