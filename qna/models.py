from django.db import models
from django.contrib.admin.models import User

# Create your models here.
class Question(models.Model):
<<<<<<< HEAD
    title       = models.CharField(max_length = 100)    # Title of question
    date        = models.DateField()                    # Day ask
    content     = models.TextField(max_length = 1000)   # Content of question
    author      = models.ForeignKey(User)               # Who is ask this question\
    likes       = models.ForeignKey(User)               # User like this question
    tags        = models.CharField(100)                 # This question can be in tags
    bonus       = models.IntegerField()                 # Bonus points of this question
=======
    title       = models.CharField(max_length = 100)                        # Title of question
    date        = models.DateField(auto_now = True)                         # Day ask
    content     = models.TextField(max_length = 1000)                       # Content of question
    author      = models.ForeignKey(User, related_name = "q_author")        # Who is ask this question
    likes       = models.ManyToManyField(User, related_name = "q_likes")    # User like this question
    tags        = models.CharField(max_length = 100)                        # This question can be in tags
    bonus       = models.IntegerField()                                     # Bonus points of this question
>>>>>>> refs/remotes/origin/master

    def __unicode__(self):
        return self.title

    def get_answers(self):
        return Answer.objects.filter(question = self)
    
class Answer(models.Model):
<<<<<<< HEAD
    date        = models.DateField()                    # Answer day
    content     = models.TextField(max_length = 1000)   # Content of answer
    author      = models.ForeignKey(User)               # Who is author of this answer
    likes       = models.ManyToManyField(User)          # Users like this answer
    question    = models.ForeignKey(Question)           # Question of this answer
=======
    date        = models.DateField(auto_now = True)                         # Answer day
    content     = models.TextField(max_length = 1000)                       # Content of answer
    author      = models.ForeignKey(User, related_name = "a_author")        # Who is author of this answer
    likes       = models.ManyToManyField(User, related_name = "a_likes")    # Users like this answer
    question    = models.ForeignKey(Question)                               # Question of this answer
>>>>>>> refs/remotes/origin/master

    def __unicode__(self):
        return self.author
