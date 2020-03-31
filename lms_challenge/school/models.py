from django.db import models
import uuid 
# Create your models here.

def generate_uniqe_id():
    key = uuid.uuid4().hex[:16].upper()
    return key

class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.IntegerField()
    

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    identification = models.CharField(max_length=20,unique=True,default=generate_uniqe_id())
    school = models.ForeignKey(School,null=True, related_name='students',on_delete=models.SET_NULL)


