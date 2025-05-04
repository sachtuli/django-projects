from django.db import models


class Project(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField(max_length=30)
    assigned_to = models.CharField(max_length=30)
    priority = models.IntegerField()
