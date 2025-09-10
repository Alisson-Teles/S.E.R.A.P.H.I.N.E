from django.db import models

# Create your models here.
class chat(models.Model):
    #host = 
    #topic =
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