from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # one to many
from django.urls import reverse 


class Post(models.Model):
    title = models.CharField(max_length=100) # A short text (like the post title)
    content = models.TextField()  # A long text (like the post body)
    date_posted = models.DateTimeField(default=timezone.now) # Auto-set when created
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)  # ✅ add this


    def __str__(self):
        return self.title
    
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # ← Add this
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    