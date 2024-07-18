from django.shortcuts import render
from .models import Post


# Create your views here.
def posts_lists(request):
    #Grabs all the posts and puts them in a list of decending date order
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts':posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post':post})