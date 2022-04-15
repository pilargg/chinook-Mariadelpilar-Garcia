from django.db import models

# Create your models here.


class Track(models.Model):
    
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField(default=0)
    bytes = models.IntegerField(default=0)
    unitPrice = models.FloatField(default=0)
    
    # associations
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Album(models.Model):
    
    title = models.CharField(max_length=200)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
     
    
class Artist(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    