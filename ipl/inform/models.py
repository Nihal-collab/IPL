from django.db import models

class Ipl(models.Model):
    team=models.CharField(max_length=100)
    captain=models.CharField(max_length=100)
    cups=models.IntegerField()


class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    branch=models.CharField(max_length=100)

