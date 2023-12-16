import io
import xlsxwriter
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import StudentDetails, ParentDetails, AcademicDetails, DocumentUpload
from .forms import (
    StudentDetailsForm,
    ParentDetailsForm,
    AcademicDetailsForm,
    DocumentUploadForm,
)
from django.views.generic import ListView
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework import viewsets
from . import serializers
from openpyxl import Workbook
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from django.urls import reverse
from wkhtmltopdf.views import PDFTemplateView
from import_export.formats import base_formats
from tablib import Dataset
from django.core.mail import send_mail
from django.conf import settings


class StudentDetailsViewSet(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all()
    serializer_class = serializers.StudentDetailsSerializer


class ParentDetailsViewSet(viewsets.ModelViewSet):
    queryset = ParentDetails.objects.all()
    serializer_class = serializers.ParentDetailsSerializer


class AcademicDetailsNormalViewSet(viewsets.ModelViewSet):
    queryset = AcademicDetails.objects.all()
    serializer_class = serializers.AcademicDetailsSerializer


class DocumentUploadViewSet(viewsets.ModelViewSet):
    queryset = DocumentUpload.objects.all()
    serializer_class = serializers.DocumentUploadSerializer


from rest_framework import generics


class AcademicDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AcademicDetailsSerializer
    queryset = AcademicDetails.objects.all()

    def get_queryset(self):
        selected_class = self.request.query_params.get("class", "")
        selected_section = self.request.query_params.get("section", "")
        selected_admission_category = self.request.query_params.get(
            "admission_category", ""
        )

        queryset = AcademicDetails.objects.all()

        if selected_class:
            queryset = queryset.filter(class_name=selected_class)

        if selected_section:
            queryset = queryset.filter(section__icontains=selected_section)

        if selected_admission_category:
            queryset = queryset.filter(
                student__admission_category__icontains=selected_admission_category
            )

        return queryset


class Display_data(View):
    def get(self, request):
        return render(request, "display_data.html")


def student_details_form(request):
    if request.method == "POST":
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            student_instance = form.save()
            return redirect(
                "student_academic_form", pk=student_instance.pk
            )  # Redirect to academic details form
    else:
        form = StudentDetailsForm()

    return render(request, "student_form.html", {"form": form})


def student_academic_detail(request, pk):
    student_instance = get_object_or_404(StudentDetails, id=pk)

    if request.method == "POST":
        form = AcademicDetailsForm(request.POST)
        if form.is_valid():
            academic_details = form.save(commit=False)
            academic_details.student = student_instance
            academic_details.save()

            # Sending email to the student
            student_mail_subject = "Welcome to Dummy School"
            student_mail_message = f"Dear {student_instance.name},\n\nYou are enrolled in Dummy School. Your Enrollment ID is {student_instance.enrollment_id}. Please provide us with the required documents for future references.\n\nTeam Dummy School"

            send_mail(
                student_mail_subject,
                student_mail_message,
                getattr(settings, "EMAIL_HOST_USER", "gujratirohan06@gmail.com"),
                [student_instance.mail_id],
            )

            # Sending email to the admin
            admin_mail_subject = "New Student Enrollment Notification"
            admin_mail_message = f"Dear Admin,\n\nYou have a new student enrolled in class {academic_details.class_name}, section {academic_details.section} with Enrollment ID {student_instance.enrollment_id} in the {academic_details.date_of_joining.year} session.\n\nBot Msg."

            send_mail(
                admin_mail_subject,
                admin_mail_message,
                getattr(settings, "EMAIL_HOST_USER", "gujratirohan06@gmail.com"),
                [getattr(settings, "ADMIN_EMAIL", "rohandass58@gmail.com")],
            )

            return redirect("display_data")  # Redirect to a success page
    else:
        form = AcademicDetailsForm(initial={"student": student_instance.id})

    return render(request, "student_academic_form.html", {"form": form})


class Home(View):
    def get(self, request):
        return render(request, "home.html")
