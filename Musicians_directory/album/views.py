from django.shortcuts import render,redirect
from album.froms import addAlbum
from .models import albumModel
# Create your views here.
def show(request):
    data = albumModel.objects.all()
    return render(request, "show.html", {"data":data})



def album(request):
    if request.method == "POST":
        form = addAlbum(request.POST)
        if form.is_valid():
            form.save() 
            return render(request, "album.html", {"form":addAlbum})
        
    return render(request, "album.html", {"form":addAlbum})

def edit(request, id ):
    data= albumModel.objects.get(id = id)
    form = addAlbum(instance= data)
    if request.method =="POST":
        form = addAlbum(request.POST, instance = data)
        if form.is_valid():
            form.save()
            return redirect("show")
        
    return render(request, "album.html", {"form":form})

def delete(request, id ):
    data = albumModel.objects.get(id = id).delete()
    return redirect("show")
    
        
