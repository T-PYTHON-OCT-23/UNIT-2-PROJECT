from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    catchy_phrase = models.CharField(max_length=200)
    description = models.TextField()

class CityImage(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='city_images/')

class CityVideo(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    video_url = models.URLField()


