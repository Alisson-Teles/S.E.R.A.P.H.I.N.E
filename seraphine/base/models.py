from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Chat(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)
    topic =  models.ForeignKey(Topic, on_delete= models.SET_NULL, null = True)
    name = models.CharField(max_length= 200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    #variable who takes the snapshots everytime this model instance was updated, so we run the save method to update this model or the specific table
    updated = models.DateTimeField(auto_now=True)
    #Everytime the save method is calld go ahead and take a time stamp

    #"auto_now_add" only save the date who this instance is created
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name 
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.body