from django.db import models
import re
# Create your models here.
class Chamber(models.Model):
	legislator = models.CharField(max_length=60)
	legislation = models.CharField(max_length=8)
	actions = models.CharField(max_length=100)
	dt =  models.CharField(max_length=10)
