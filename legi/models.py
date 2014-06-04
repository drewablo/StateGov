from django.db import models
import re
# Create your models here.
class Chamber(models.Model):
	legislator = models.CharField(max_length=60)
	legislation = models.CharField(max_length=8)
	actions = models.CharField(max_length=100)
	dt =  models.CharField(max_length=10)
	party = models.CharField(max_length=1)
	
	def billNumber(self):
		return self.legislation
	def name(self):
		return self.legislator
	def date(self):
		return self.dt
	def pol(self):
		return self.party

class Votes(models.Model):
	legislator = models.CharField(max_length=60)
	legislation = models.CharField(max_length=8)
	vote = models.CharField(max_length=4)
