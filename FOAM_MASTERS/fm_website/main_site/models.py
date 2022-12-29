from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subscriber(models.Model):
	email = models.EmailField(null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email

class MailMassage(models.Model):
	subject = models.CharField(null=True, max_length=100)
	body = models.TextField(null=True)

	def __str__(self):
		return self.subject
	