from django.shortcuts import render
from .models import Employee


def employeeData(req):
    employee = Employee.objects.all()
    empDict = {"employees": employee}
    return render(req, "empApp/employees.html", empDict)
