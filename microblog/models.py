from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)
