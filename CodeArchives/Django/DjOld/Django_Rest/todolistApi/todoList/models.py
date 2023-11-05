from django.db import models
from authentication.models import User
from helpers.models import TrackingModel

class TodoList(TrackingModel):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

        
    

