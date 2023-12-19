from django.db import models
from musician.models import MusiciansModel
# Create your models here.
class albumModel(models.Model) :
    AlbumName = models.CharField(max_length=100)
    date =models.DateField(max_length=100)
    rating = models.CharField(max_length = 2)
    musician = models.OneToOneField(MusiciansModel,on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.AlbumName
