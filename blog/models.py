from django.db import models
# Create your blog models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription= models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.title