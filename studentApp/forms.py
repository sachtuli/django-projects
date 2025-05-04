from django import forms
from studentApp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "firstName": "First Name",
            "lastName": "Last Name",
            "testScore": "Test Score",
        }
