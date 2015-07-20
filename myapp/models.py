from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    mobile = models.IntegerField()

    def __unicode__(self):
        return self.name

class Education(models.Model):
    e_id=models.ForeignKey(User)
    degree =models.CharField(max_length=100)
    percentage =models.CharField(max_length=100)
    college =models.CharField(max_length=100)


class Question(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    city =models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
   
    degree = models.CharField(max_length=30)
    percentage = models.CharField(max_length=30)
    college = models.CharField(max_length=30)


"""class Category(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=30)
   
    def __unicode__(self):
        return self.name"""
