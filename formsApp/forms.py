from django import forms
from django.core import validators

# custom validation


class UserRegistrationForm(forms.Form):
    Gender = [("male", "MALE"), ("female", "FEMALE")]
    firstName = forms.CharField(validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(20)])
    lastName = forms.CharField(validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(10)])
    age = forms.IntegerField(validators=[validators.MinValueValidator(18), validators.MaxValueValidator(100)])
    gender = forms.CharField(widget=forms.Select(choices=Gender))

    # def clean(self):
    #     user_cleaned_data = super().clean()
    #     inputFirstName = user_cleaned_data["firstName"]
    #     inputLastName = user_cleaned_data["lastName"]
    #     if len(inputFirstName) > 20 or len(inputLastName) > 20:
    #         raise forms.ValidationError("Max Length allowed is 20")

    # def custom validation

    # def clean_firstName(self):
    #     inputFirstname = self.cleaned_data["firstName"]
    #     if len(inputFirstname) > 20:
    #         raise forms.ValidationError("Max Length allowed is 20")
    #     return inputFirstname
