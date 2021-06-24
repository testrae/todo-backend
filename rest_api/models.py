from django.db import models

# Create your models here.

class ToDoItem(models.Model):

    text = models.CharField(max_length=255)
    done = models.BooleanField()