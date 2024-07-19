from django.urls import path
from . import views
# How you designate a url page from one another
app_name = 'posts'

urlpatterns = [
    path('', views.posts_lists, name="list"),
    path('new-post/', views.post_new, name="new-post"),
    path('<slug:slug>', views.post_page, name="page"),
]
