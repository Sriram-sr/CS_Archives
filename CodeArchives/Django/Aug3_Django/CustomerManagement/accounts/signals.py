# signals for registered user added to users group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def addgroup(sender, instance, created, **kwargs):
    print('signal working') # tested working

