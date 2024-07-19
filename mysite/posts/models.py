from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    #ImageField requires Pillow to be installed
    banner = models.ImageField(default='fallback.png', blank=True)
    # py manage.py makemigrations is required when updating a model. Must migrate after
    #This is an example of a many to one relational database. Cascade means delete all the posts from a user if a user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.title
    