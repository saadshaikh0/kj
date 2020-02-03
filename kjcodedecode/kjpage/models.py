from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class question(models.Model):
    text=models.TextField(max_length=200)

    def __str__(self):
        return self.text
class answer(models.Model):
    text=models.TextField(max_length=50)
    status=models.BooleanField()
    question=models.ForeignKey(question,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Student(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)
    time=models.TextField(max_length=10,default="")