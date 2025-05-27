from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model): # User Profile Model
    user = models.OneToOneField(User, on_delete=models.CASCADE) # This creates a one-to-one relationship with the User model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # Image field for the user profile
    bio = models.TextField(blank=True, null=True) # Bio field for the user profile
    location = models.CharField(max_length=100, blank=True, null=True) # Location field for the user profile
    birth_date = models.DateField(null=True, blank=True) # Birth date field for the user profile

    def __str__(self): # String representation of the Profile model 
        return f'{self.user.username} Profile'