from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subscriber(models.Model):
	email = models.EmailField(null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email

class SentMail(models.Model):
	subject = models.CharField(null=True, max_length=100)
	body = models.TextField(null=True)

	def __str__(self):
		return self.subject

class RecievedMail(models.Model):
	name = models.CharField(null=True, max_length=100)
	email = models.EmailField(null=True, max_length=254)
	subject = models.CharField(null=True, max_length=100)
	message = models.TextField(null=True)

	def __str__(self):
		return self.subject
	