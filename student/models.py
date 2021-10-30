from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    name = models.CharField('NAME', max_length=100, blank=False)
    major = models.CharField('MAJOR', max_length=100, blank=False)
    studentnum = models.CharField('STUDENTNUM', max_length=100, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)


    def get_absolute_url(self):
       return reverse('student:student_detail', args=(self.id,))