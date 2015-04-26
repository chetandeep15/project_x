from django.db import models

# Create your models here.
class Market(models.Model):
	"""docstring for Stocks"""
	name=models.CharField(max_length=255)
	date=models.DateField()
	open=models.FloatField()
	high=models.FloatField()
	low=models.FloatField()
	close=models.FloatField()
	volume=models.BigIntegerField()
	adj_close=models.FloatField()
	

class Currency(models.Model):
	"""docstring for Currency"""
	
	name=models.CharField(max_length=255)
	date=models.DateField()
	high=models.FloatField()
	low=models.FloatField()
	close=models.FloatField()

class Companies(models.Model):
	"""docstring for Companies"""

	name=models.CharField(max_length=255)
	date=models.DateField()
	open=models.FloatField()
	high=models.FloatField()
	low=models.FloatField()
	close=models.FloatField()
	volume=models.BigIntegerField()
	adj_close=models.FloatField()