from django.db import models
from django.utils import timezone
from martor.models import MartorField

# Create your models here.

class Main(models.Model):
    """Content for the index page"""
    content = MartorField()
    
    def __str__(self):
        return self.content

class Category(models.Model):
    """Categories for the entries"""
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    """Entries for the blog"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = MartorField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        if len(self.content) < 100:
            return self.content
        else:
            return self.content[0:100] + '...'
        
