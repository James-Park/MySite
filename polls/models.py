import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# After writing models.py file, execute the follow command
# py manage.py makemigrations polls

# If you execute the follow command, the tables of models will be created.
# py manage.py migrate

# insert a data into Question Model
# py manage.py shell
# >>> from polls.models import Choice, Question
# >>> Question.objects.all()
# >>> from django.utils import timezone
# >>> from django.utils import timezone
# >>> q = Question(question_text="What is new?", pub_date=timezone.now())
# >>> q.save()
# >>> q.id
# >>> Question.objects.get(id=1)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text