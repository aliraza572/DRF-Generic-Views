from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    city = models.CharField(max_length=200)
    join = models.DateField()
    country = models.CharField(max_length=200, default=None, blank=True, null=True) # newly fiel added

    def __str__(self):
        return self.name
