from urllib.request import Request
from django.shortcuts import render
from . import forms


def userRegistrationView(req: Request):
    form = forms.UserRegistrationForm()
    if req.method == "POST":
        form = forms.UserRegistrationForm(req.POST)
        if form.is_valid():
            print("Form is Valid")
            print("FirstName", form.cleaned_data["firstName"])

    return render(req, "formsApp/userRegistration.html", {"form": form})
