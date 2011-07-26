from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
                    ('M', 'Male'),
                    ('F', 'Female'),
                 )
class Profile(models.Model):
    '''
    The detail information of user
    '''
    user         = models.ForeignKey(User, unique = True)
    website      = models.URLField(max_length = 200, blank = True)
    birthday     = models.DateField()
    home_address = models.CharField(max_length = 200, blank = True)
    work_address = models.CharField(max_length = 200, blank = True)
    gender       = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    education    = models.TextField(blank = True)
    avatar       = models.ImageField(upload_to = 'image', blank = True)
    about_user   = models.TextField(blank = True)
    home_phone   = models.CharField(max_length = 15, blank = True)
    work_phone   = models.CharField(max_length = 15, blank = True)
    mobile_phone = models.CharField(max_length = 15, blank = True)
    interests    = models.TextField(blank = True)
    joined_date  = models.DateField(auto_now = True)
    
    def get_experience(self):
        return Experience.objects.filter(user = self)
    
    def __unicode__(self):
        return self.user.username
    
    
class Experience(models.Model):
    '''
    Experience working of user
    '''
    user = models.ForeignKey(User, unique = True)
    


