from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    user_id = models.ForeignKey(User, unique = True)
    website = models.CharField(max_length = 200)


