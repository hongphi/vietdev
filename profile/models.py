from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
                  ('M', 'Male'),
                  ('F', 'Female'),
                 )

WORK_TIME_CHOICES = (
                     (1, 'less 1 year'),
                     (2, '1 - 2 years'),
                     (3, '2 - 3 years'),
                     (4, '3 - 4 years'),
                     (5, 'over 5 years'),
                    )
class Profile(models.Model):
    '''
    The detail information of user
    '''
    user         = models.ForeignKey(User, unique = True)
    first_name   = models.CharField(max_length = 15, blank = True)
    middle_name  = models.CharField(max_length = 15, blank = True)
    last_name    = models.CharField(max_length = 15, blank = True)    
    website      = models.URLField(max_length = 50, blank = True)
    birthday     = models.DateField()
    home_address = models.CharField(max_length = 100, blank = True)
    work_address = models.CharField(max_length = 100, blank = True)
    gender       = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    education    = models.TextField(blank = True)
    avatar       = models.ImageField(upload_to = 'image', blank = True)
    about_user   = models.TextField(blank = True)
    home_phone   = models.CharField(max_length = 15, blank = True)
    work_phone   = models.CharField(max_length = 15, blank = True)
    mobile_phone = models.CharField(max_length = 15, blank = True)
    interests    = models.TextField(blank = True)
    joined_date  = models.DateTimeField(auto_now = True)
    
    def get_experience(self):
        return Experience.objects.filter(user = self)
    
    def __unicode__(self):
        return self.user.username
    

    
class Experience(models.Model):
    '''
    Experience working of user
    '''
    id            = models.AutoField(primary_key = True)
    user          = models.ForeignKey(User, unique = False)
    position      = models.CharField(max_length = 50)
    company_name  = models.CharField(max_length = 100)
    technical_use = models.CharField(max_length = 100)
    work_time     = models.IntegerField(choices = WORK_TIME_CHOICES)
    work_details  = models.TextField() 
    logo          = models.ImageField(upload_to = "image", blank = True)
    
    def __unicode__(self):
        return self.user.username
    

class Activity(models.Model):
    user = models.ForeignKey(User, unique = True)
    level = models.IntegerField(default = 0)
    special_point = models.IntegerField(default = 0)    


