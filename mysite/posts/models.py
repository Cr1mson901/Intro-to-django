from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    #ImageField requires Pillow to be installed
    banner = models.ImageField(default='fallback.png', blank=True)
    # py manage.py makemigrations is required when updating a model. Must migrate after
    
    def __str__(self):
        return self.title
    