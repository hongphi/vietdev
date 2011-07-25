from django.db import models
from django.contrib.admin.models import User

# Create your models here.
class Question(models.Model):
    title       = models.CharField(max_length = 100)    # Title of question
    date        = models.DateField()                    # Day ask
    content     = models.TextField(max_length = 1000)   # Content of question
    author      = models.ForeignKey(User)               # Who is ask this question\
    likes       = models.ForeignKey(User)               # User like this question
    tags        = models.CharField(100)                 # This question can be in tags
    bonus       = models.IntegerField()                 # Bonus points of this question

    def __unicode__(self):
        return self.title

    def get_answers(self):
        return Answer.objects.filter(question = self)
    
class Answer(models.Model):
    date        = models.DateField()                    # Answer day
    content     = models.TextField(max_length = 1000)   # Content of answer
    author      = models.ForeignKey(User)               # Who is author of this answer
    likes       = models.ManyToManyField(User)          # Users like this answer
    question    = models.ForeignKey(Question)           # Question of this answer

    def __unicode__(self):
        return self.author
