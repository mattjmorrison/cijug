from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username + ": " + self.message