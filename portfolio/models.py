from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    discription= models.CharField(max_length=250)
    image= models.ImageField(upload_to='portfolio/image/')
    url=models.URLField(blank=True)
    
    def __str__(self):
        return self.title
class Course(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/image/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/image/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
class Galary(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/image/')
    
    def __str__(self):
        return self.title
class Doc(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/image/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
