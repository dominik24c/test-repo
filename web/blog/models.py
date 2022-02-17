from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
