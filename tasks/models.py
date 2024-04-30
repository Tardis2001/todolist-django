from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    # decription = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.title
class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name