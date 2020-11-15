from django.db import models

# Create your models here.
class Student(models.Model): #ORM will convert to table use small letters.
    name = models.TextField(default=None)
    email = models.EmailField(default=None)
    pw = models.TextField(default=None)
    sub = models.TextField(default=None)
    mobile = models.BigIntegerField(default=0)
