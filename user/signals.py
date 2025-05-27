from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Profile 

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
# Connect the signal to create a profile when a User is created


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
# Connect the signal to save the profile when a User is saved