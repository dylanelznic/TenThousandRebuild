from django.db import models

# Create your models here.
class Activity(models.Model):
	text = models.TextField(default='')