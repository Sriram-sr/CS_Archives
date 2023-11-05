from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True) # null is true in db beacause on deleting topic\
    # it is set for the room to be null so database should allow them
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    updated = models.DateTimeField(auto_now=True)  # this will add a timestamp that gets updated when in a change
    created = models.DateTimeField(auto_now_add=True) # this will upload a timestamp that will not change

    class Meta:
        ordering = ['-created', '-updated']
        
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)       
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created','-updated']

    def __str__(self):
        return self.body[0:50]