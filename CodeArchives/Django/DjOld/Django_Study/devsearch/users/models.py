from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/', default="profiles/profile.jpg")
    social_github = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.username

class Skill(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name  = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

# @receiver(post_save, sender=User)
def profileUpdated(sender, instance, created, **kwargs):
    if created:
        # for creating profile
        print('user saved')
        user = instance
        profile = Profile.objects.create(
            user=user,
            # name=user.first_name,
            email=user.email,
            username=user.username,
        )
        # for sending mail 
        subject = "Sending email for registering new user"
        message = "Hurray!!!!....You have done it"
        user=instance

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    else:
        user = instance
        profile = Profile.objects.get(user=user)
        name = instance.username
        print(name)
        profile.username = name
        profile.user = instance
        profile.save()

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **anyvar):
    user=instance.user
    user.delete()

post_save.connect(profileUpdated, sender=User)
# post_delete.connect(deleteUser, sender=Profile)