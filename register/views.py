# app_name/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Class, Student
from .forms import ClassForm, StudentForm


def class_list(request):
    classes = Class.objects.all()
    return render(request, "register/class_list.html", {"classes": classes})


def class_detail(request, pk):
    class_instance = get_object_or_404(Class, pk=pk)
    students = class_instance.student_set.all()
    return render(
        request,
        "register/class_detail.html",
        {"class_instance": class_instance, "students": students},
    )


def class_new(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            class_instance = form.save()
            return redirect("class_detail", pk=class_instance.pk)
    else:
        form = ClassForm()
    return render(request, "register/class_new.html", {"form": form})


def class_edit(request, pk):
    class_instance = get_object_or_404(Class, pk=pk)
    if request.method == "POST":
        form = ClassForm(request.POST, instance=class_instance)
        if form.is_valid():
            class_instance = form.save()
            return redirect("class_detail", pk=class_instance.pk)
    else:
        form = ClassForm(instance=class_instance)
    return render(request, "register/class_edit.html", {"form": form})


def class_delete(request, pk):
    class_instance = get_object_or_404(Class, pk=pk)
    class_instance.delete()
    return redirect("class_list")


#########################################################################################################################


def student_detail(request, pk):
    student_instance = get_object_or_404(Student, pk=pk)
    return render(
        request, "register/student_detail.html", {"student_instance": student_instance}
    )


def student_list(request):
    students = Student.objects.all()
    return render(request, "register/class_detail.html", {"students": students})


def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student_instance = form.save()
            return redirect("student_detail", pk=student_instance.pk)
    else:
        form = StudentForm()
    return render(request, "register/student_new.html", {"form": form})

def student_edit(request, pk):
    student_instance = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student_instance)
        if form.is_valid():
            student_instance = form.save()
            return redirect("class_detail", pk=student_instance.stud_Class.pk)
    else:
        form = StudentForm(instance=student_instance)
    return render(request, "register/student_edit.html", {"form": form})

def student_delete(request, pk):
    student_instance = get_object_or_404(Student, pk=pk)
    student_instance.delete()
    return redirect('class_detail', pk=student_instance.stud_Class.pk)
