from django.db import models

# Create your models here.

class You(models.Model):
    your_Name = models.CharField(max_length=100, default='')
    your_Major= models.CharField(max_length=200, default='')
    your_MBTI= models.CharField(max_length=100, default='')
    your_Favorite= models.CharField(max_length=100, default='')
    your_Age= models.IntegerField(default=0)
