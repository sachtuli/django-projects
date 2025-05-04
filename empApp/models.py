from django.db import models


class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=50)


class Programmer(models.Model):
    name = models.CharField(max_length=30)
    salary = models.FloatField()
    language = models.CharField(max_length=30)


class Project(models.Model):
    name = models.CharField(max_length=30)
    programmers = models.ManyToManyField(Programmer)


class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=15)


class PhoneNumber(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Person(models.Model):
    name: models.CharField(max_length=30)
    age: models.IntegerField()
    address: models.CharField(max_length=50)
    city: models.CharField(max_length=30)
    state: models.CharField(max_length=30)
    zipcode: models.IntegerField()


class License(models.Model):
    number = models.CharField(max_length=15)
    validFrom = models.DateField()
    validTo = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
