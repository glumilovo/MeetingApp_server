from django.db import models


class User(models.Model):
    email = models.TextField(max_length=128)
    password = models.TextField()
    name = models.TextField()
    surname = models.TextField()
    city = models.TextField()


class Message(models.Model):
    senderEmail = models.TextField()
    targetEmail = models.TextField()
    message = models.TextField()

# Create your models here.
