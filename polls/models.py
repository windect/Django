from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days= 1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolan = True
        was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Etc(models.Model):
    question_etc = models.ForeignKey(Question, on_delete=models.CASCADE)
    Etc_text = models.CharField(max_length = 300)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.Etc_text