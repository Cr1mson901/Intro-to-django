from django.urls import path
from . import views
# How you designate a url page from one another
app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
]
