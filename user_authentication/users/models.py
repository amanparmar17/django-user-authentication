from django.db import models

class Student(models.Model):
	name=models.CharField(max_length=10)
	age=models.IntegerField(default=0)
	address=models.CharField(max_length=100)
	enrollment=models.IntegerField(default=0)

	def __str__(self):
		return self.name

