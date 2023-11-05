from django.db import models

class UserProfile(models.Model):
    image = models.ImageField(upload_to="data")
    # for this you have to specify MEDIA_ROOT in settings file as you create a folder in project level and 
    # add a path joining base dir 
