from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def posts_lists(request):
    #Grabs all the posts and puts them in a list of decending date order
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts':posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post':post})

#Decorator checks if a user is logged in. If not then it redirects them to /users/login/
@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == "POST":
        # Need .FILES because we are sending an image file too
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            #Gets the user that is logged in and adds it to the post object
            newpost.author = request.user
            # Saves the post
            newpost.save()
            return redirect("posts:list")
    else:        
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})