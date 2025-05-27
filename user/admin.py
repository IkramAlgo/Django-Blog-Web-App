from django.contrib import admin
from .models import Profile


# Register your models here.

admin.site.register(Profile)
# This code registers the Profile model with the Django admin site, allowing it to be managed through the admin interface.
# This is useful for managing user profiles directly from the admin dashboard.
