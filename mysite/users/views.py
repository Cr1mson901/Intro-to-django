from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def register_view(request):
    #Checks if the form has been submitted with information
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # If the form is valid, it saves
        if form.is_valid():
            # Logs in after register
            login(request, form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #Logs in if valid
            login(request, form.get_user())
            return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})