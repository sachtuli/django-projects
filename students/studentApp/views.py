from django.shortcuts import render
from studentApp.models import Student
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class StudentListView(ListView):
    model = Student
    # default template name: studentApp/student_list.html
    # default context object name: student_list


@method_decorator(login_required, name="dispatch")
class StudentDetailView(DetailView):
    model = Student
    # default template name: studentApp/student_detail.html
    # default context object name: student


@method_decorator(login_required, name="dispatch")
class createStudentView(CreateView):
    model = Student
    fields = ("firstName", "lastName", "testScore")


@method_decorator(login_required, name="dispatch")
class updateStudentView(UpdateView):
    model = Student
    fields = ("testScore",)


@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("studentApp.delete_student"), name="dispatch")
class deleteStudentView(DeleteView):
    model = Student
    success_url = reverse_lazy("students")


def logout_view(request):
    return render(request, "registration/logout.html")
