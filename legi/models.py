from django.db import models

# Create your models here.
class Chamber(models.Model):
	legislator = models.CharField(max_length=60)
	legislation = models.CharField(max_length=8)
	actions = models.CharField(max_length=100)
	dt =  models.CharField(max_length=10)
	def __str__(self):
		return self.legislator
