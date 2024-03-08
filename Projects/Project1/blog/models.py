from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    asignature = models.CharField(max_length=60, default= "not enrrolled")
    phone = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField("date published")
    
class Question(models.Model):
    question_text = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student,on_delete= models.CASCADE)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    
