from django.shortcuts import render
from .forms import addmusicianform
# Create your views here.

def add(request):
    if request.method == "POST":
        form = addmusicianform(request.POST)
        if form.is_valid():
            form.save() 
            return render(request, "add.html", {"form":addmusicianform})
        
    return render(request, "add.html", {"form":addmusicianform})
