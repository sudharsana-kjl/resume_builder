from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#resume_file = models.FileField(upload_to = 'books')
	name = models.CharField(max_length = 200)
	address = models.CharField(max_length = 2000, default = "/")
# Create your models here.
