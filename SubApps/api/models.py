from django.db import models


# Create your models here.
class Birthday(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    note = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Password(models.Model):
    website = models.CharField(max_length=40)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.website


class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    todoText = models.CharField(max_length=100)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.todoText
