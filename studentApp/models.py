from django.db import models
from django.urls import reverse


class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    testScore = models.FloatField()

    def __str__(self):
        return self.firstName

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
