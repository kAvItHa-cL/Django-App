from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

class choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text