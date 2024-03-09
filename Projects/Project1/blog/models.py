from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    asignature = models.CharField(max_length=60, default= "not enrrolled")
    phone = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField("date published")
    def __str__(self):
        return self.first_name , self.last_name , self.asignature, self.phone , self.date
    
class Question(models.Model):
    question_text = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student,on_delete= models.CASCADE)
    def __str__(self):
        return self.question_text, self.pub_date, self.student


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text, self.choice_text, self.votes

    
