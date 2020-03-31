from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.IntegerField()
    

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    identification = models.CharField(max_length=20,unique=True)
    school = models.ForeignKey(School,null=True, related_name='students',on_delete=models.SET_NULL)


