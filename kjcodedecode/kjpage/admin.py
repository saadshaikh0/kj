from django.contrib import admin
from .models import question,answer,Student
# Register your models here.
admin.site.register(question)
admin.site.register(answer)
admin.site.register(Student)