from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Submit(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    sol = models.FileField(upload_to='submits/', blank=True, null=True)
    verdict = models.CharField(max_length = 50, blank=True, null=True)
    def __str__(self):
        return self.user.username