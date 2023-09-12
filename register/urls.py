from django.urls import path
from . import views

urlpatterns = [
    path("", views.class_list, name="class_list"),
    path("class/<int:pk>/", views.class_detail, name="class_detail"),
    path("class/new/", views.class_new, name="class_new"),
    path("class/edit/<int:pk>/", views.class_edit, name="class_edit"),
    path("class/delete/<int:pk>/", views.class_delete, name="class_delete"),
    path("students/", views.student_list, name="student_list"),
    path("students/<int:pk>/", views.student_detail, name="student_detail"),
    path("students/new/", views.student_new, name="student_new"),
    path("students/edit/<int:pk>/", views.student_edit, name="student_edit"),
    path("students/delete/<int:pk>/", views.student_delete, name="student_delete"),
]
