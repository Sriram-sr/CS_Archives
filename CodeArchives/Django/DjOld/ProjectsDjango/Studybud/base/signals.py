from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Profile

def createProfile(sender,instance,created,**kwargs):
    if created:
        profile = Profile.objects.create(
            user = instance,
            name = instance.username
        )

post_save.connect(createProfile,sender=User)    