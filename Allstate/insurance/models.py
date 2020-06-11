from django.db import models

# Create your models here.

class AddCustomer(models.Model):
	name = models.CharField(max_length=150, primary_key=True)
	age = models.IntegerField()
	salary = models.IntegerField()
	company = models.CharField(max_length=300)
	insurance_type = models.CharField(max_length=150)
	
	def __str__(self):
		return self.name