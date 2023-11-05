from time import timezone
from django.db import models
from django.forms import SlugField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    options = (
        ('draft','Draft'),
        ('published','Published'),
    )

    title = models.CharField(max_length=100)
    slug = SlugField(max_length=200)
    Publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options,default = 'draft')