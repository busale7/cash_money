from django.db import models

# Create your models here.
class Business(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	established = models.DateField()

	def __str__(self) :
		return self.name
		