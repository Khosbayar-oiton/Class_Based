# app_name/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Class, Student
from .forms import ClassForm, StudentForm


def class_list(request):
    classes = Class.objects.all()
    return render(request, 'register/class_list.html', {'classes': classes})

def class_detail(request, pk):
    class_instance = get_object_or_404(Class, pk=pk)
    return render(request, 'register/class_detail.html', {'class_instance': class_instance})

def class_new(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            class_instance = form.save()
            return redirect('class_detail', pk=class_instance.pk)
    else:
        form = ClassForm()
    return render(request, 'register/class_edit.html', {'form': form})

# def class_create(request):
#     if request.method == 'POST':
#         form = ClassForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('class_list')
#     else:
#         form = ClassForm()
#     return render(request, 'class_form.html', {'form': form})

# def class_update(request, pk):
#     class_instance = get_object_or_404(Class, pk=pk)
#     if request.method == 'POST':
#         form = ClassForm(request.POST, instance=class_instance)
#         if form.is_valid():
#             form.save()
#             return redirect('class_list')
#     else:
#         form = ClassForm(instance=class_instance)
#     return render(request, 'class_form.html', {'form': form})

# def class_delete(request, pk):
#     class_instance = get_object_or_404(Class, pk=pk)
#     if request.method == 'POST':
#         class_instance.delete()
#         return redirect('class_list')
#     return render(request, 'class_confirm_delete.html', {'class_instance': class_instance})


# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'student_list.html', {'students': students})

# # Detail view for a single student
# def student_detail(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     return render(request, 'register/student_detail.html', {'student': student})

# # Create view for adding a new student
# def student_create(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm()
#     return render(request, 'student_form.html', {'form': form})

# # Update view for editing an existing student
# def student_update(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm(instance=student)
#     return render(request, 'student_form.html', {'form': form})

# # Delete view for removing a student
# def student_delete(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'POST':
#         student.delete()
#         return redirect('student_list')
#     return render(request, 'student_confirm_delete.html', {'student': student})