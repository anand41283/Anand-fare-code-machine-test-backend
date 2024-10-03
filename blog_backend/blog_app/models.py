from django.db import models
from django.contrib.auth.models import AbstractUser

class Customuserdb(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.username

class BlogPost(models.Model):
    author = models.ForeignKey(Customuserdb, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


