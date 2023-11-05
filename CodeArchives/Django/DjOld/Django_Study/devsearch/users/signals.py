from django.db.models.signals import post_delete

def profileUpdated(sender,instance,created,**kwargs):
    print("Profile Updated")
