from django.shortcuts import render
from modelForms.models import Project
from modelForms.forms import ProjectForm


def index(req):
    return render(req, "modelForms/index.html")


def listProjects(req):
    projects = Project.objects.all()
    return render(req, "modelForms/listprojects.html", {"projects": projects})


def addProject(req):
    form = ProjectForm()
    if req.method == "POST":
        form = ProjectForm(req.POST)
        if form.is_valid():
            form.save()
            return listProjects(req)
        return index(req)
    return render(req, "modelForms/addProject.html", {"form": form})
