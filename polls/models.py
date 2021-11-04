from django.db import models

# Create your models here.

class Register(models.Model):
    username=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    topic = models.CharField(max_length=1000)
    choice_one = models.CharField(max_length=1000)
    choice_two = models.CharField(max_length=1000)
    choice_three = models.CharField(max_length=1000)
    choice_four = models.CharField(max_length=1000)
    choice_one_vote = models.IntegerField(max_length=100)
    choice_two_vote = models.IntegerField(max_length=100)
    choice_three_vote = models.IntegerField(max_length=100)
    choice_four_vote = models.IntegerField(max_length=100)
    poll_date = models.DateField()
    poll_status = models.BooleanField()

class CheckVote(models.Model):
    username = models.CharField(max_length=50)
    topic_id = models.IntegerField()