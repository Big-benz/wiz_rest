from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(default = None, max_length = 100)
    age = models.IntegerField()
    role = models.CharField(default = None, max_length = 100)
    staff_number = models.IntegerField()

    def __str__(self):
        return self.name
