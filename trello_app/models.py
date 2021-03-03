from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# ORM
# Object Relational Mapper
# class => table in DB
# fields/attributes => columns in tables
# object => map to rows in the table

# instance of the class is an object

# inherit from the Model class provided by Django
# Vehicle (base class) => Car, Truck, Bicycle (child classes)

# OOP concept, Inheritance: reuse the code
# model is the base class
# Task is the child class

# we want to reuse some properties of Django models in our task class


class TaskList(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(
    default=timezone.now
  )
  # user_id, who has created this list?
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # dunder str, magic method
  def __str__(self): # toString()
    return f"{self.name} ---- {self.created_at}"

# class -> Table
# fields -> Columns in the table (fields part of Django Model class)
class Task(models.Model):
  # trello_app_task
  # column_name, type of the column: VARCHAR(50)
  name = models.CharField(max_length=50)
  desc = models.TextField()
  created_at = models.DateTimeField(
    default=timezone.now
  )
  due_date = models.DateTimeField()
  # change made
  # list_id
  list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name} --- {self.desc}"