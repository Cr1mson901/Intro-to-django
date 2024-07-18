from django.urls import path
from . import views
# How you designate a url page from one another
app_name = 'users'

urlpatterns = [
    path('', views.register, name="register"),
]
