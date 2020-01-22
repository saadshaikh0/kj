from django.db import models

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