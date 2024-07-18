from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    #Checks if the form has been submitted with information
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # If the form is valid, it saves
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })