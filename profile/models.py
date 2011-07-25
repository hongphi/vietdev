from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    '''
    The detail information of user
    '''
    user         = models.ForeignKey(User, unique = True)
    website      = models.URLField(max_length = 200, null = True, blank = True)
    birthday     = models.DateField()
    home_address = models.CharField(max_length = 200, null = True, blank = True)
    work_address = models.CharField(max_length = 200, null = True, blank = True)
    gender       = models.CharField(max_length = 2)
    education    = models.TextField(null = True, blank = True)
    avatar       = models.ImageField(upload_to = 'image', null = True, blank = True)
    about_user   = models.TextField(null = True, blank = True)
    home_phone   = models.CharField(max_length = 15)
    work_phone   = models.CharField(max_length = 15)
    mobile_phone = models.CharField(max_length = 15)
    interests    = models.TextField(null = True, blank = True)
    joined_date  = models.DateField(auto_now = True)
    
    def __unicode__(self):
        return self.user.username
    
    
class Experience(models.Model):
    '''
    Experience working of user
    '''
    user = models.ForeignKey(User, unique = True)
    


