
from tkinter import CASCADE
from django.db import models

# Create your models here.
class categry(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.title
class image(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    cat=models.ForeignKey(categry, on_delete=models.CASCADE)
    def __str__(self):
        return self.title