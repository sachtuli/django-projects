from django.shortcuts import render


def render_template(req):
    return render(req, "templatesApp/firstTemplate.html")
