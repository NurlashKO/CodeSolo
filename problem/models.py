from django.db import models

# Create your models here.

class Problem(models.Model):
    name = models.CharField(max_length = 100)
    statement = models.TextField()
    in_example = models.TextField(max_length = 200)
    out_example = models.TextField(max_length = 200)
    acc_sol = models.TextField()
    test_in = models.FileField(upload_to="tests/")
    test_out = models.FileField(upload_to="tests/")
    def __str__(self):
        return self.name
