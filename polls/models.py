import datetime
from django.db import models
from django.utils import timezone

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    def __str__(self):
        return self.tag_name
    is_active = models.BooleanField (default=False)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    tags = models.ManyToManyField(Tag)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
    votes = models.IntegerField(default=0)



    
