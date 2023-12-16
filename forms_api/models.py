import random
from django.db import models
from datetime import datetime


class StudentDetails(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    ADMISSION_CATEGORY_CHOICES = [
        ("General", "General"),
        ("SC", "SC"),
        ("ST", "ST"),
        ("OBC", "OBC"),
    ]

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    adhar_card_number = models.CharField(max_length=16)
    dob = models.DateField(default=datetime.now())
    identification_marks = models.TextField()
    admission_category = models.CharField(
        max_length=50, choices=ADMISSION_CATEGORY_CHOICES
    )
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    mail_id = models.EmailField()
    contact_detail = models.CharField(max_length=20)
    address = models.TextField()

    enrollment_id = models.CharField(
        max_length=12,
        unique=True,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # Generate enrollment ID on save
        if not self.enrollment_id:
            self.enrollment_id = self.generate_enrollment_id()
        super().save(*args, **kwargs)

    def generate_enrollment_id(self):
        # Generate enrollment ID based on the specified format
        date_part = self.dob.strftime("%d%m%y")
        name_part = self.name[:3].upper()
        random_part = f"{random.randint(1, 999):03}"
        return f"{date_part}{name_part}{random_part}"

    def __str__(self):
        return f"{self.name} {self.enrollment_id}"


class AcademicDetails(models.Model):
    student = models.ForeignKey(
        StudentDetails, on_delete=models.CASCADE, related_name="academic_details"
    )
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    date_of_joining = models.DateField(default=datetime.now())


class DocumentUpload(models.Model):
    student = models.ForeignKey(
        StudentDetails,
        on_delete=models.CASCADE,
    )
    document = models.FileField(upload_to="documents/")


class ParentDetails(models.Model):
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=255)
    father_qualification = models.CharField(max_length=255)
    father_profession = models.CharField(max_length=255)
    father_designation = models.CharField(max_length=255)
    father_aadhar_card = models.CharField(max_length=16)
    father_mobile_number = models.CharField(max_length=20)
    father_mail_id = models.EmailField()

    mother_name = models.CharField(max_length=255)
    mother_qualification = models.CharField(max_length=255)
    mother_profession = models.CharField(max_length=255)
    mother_designation = models.CharField(max_length=255)
    mother_aadhar_card = models.CharField(max_length=16)
    mother_mobile_number = models.CharField(max_length=20)
    mother_mail_id = models.EmailField()
