from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(Member)
    day = models.DateField()
    num_of_answers = models.IntegerField()

    def __unicode__(self):
        return self.title
