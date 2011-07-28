from django.db import models
from django.contrib.admin.models import User

# Create your models here.
class Question(models.Model):
    title       = models.CharField(max_length = 100)                                        # Title of question
    date        = models.DateField(auto_now = True)                                         # Day ask
    content     = models.TextField(max_length = 1000)                                       # Content of question
    author      = models.ForeignKey(User, related_name = "q_author")                        # Who is ask this question
    likes       = models.ManyToManyField(User, related_name = "q_likes", blank = True)      # User like this question
    tags        = models.CharField(max_length = 100, blank = True)                          # This question can be in tags
    bonus       = models.IntegerField(default = 0)                                          # Bonus points of this question

    def __unicode__(self):
        return self.title

    def get_answers(self):
        return Answer.objects.filter(question = self)

    def count_answers(self):
        return Answer.objects.filter(question = self).count()
    
class Answer(models.Model):
    date        = models.DateField(auto_now = True)                         # Answer day
    content     = models.TextField(max_length = 1000)                       # Content of answer
    author      = models.ForeignKey(User, related_name = "a_author")        # Who is author of this answer
    likes       = models.ManyToManyField(User, related_name = "a_likes", blank = True)    # Users like this answer
    question    = models.ForeignKey(Question)                               # Question of this answer

    def __unicode__(self):
        return self.author.username
