from rest_framework import serializers
from .models import StudentDetails, ParentDetails, AcademicDetails, DocumentUpload


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = "__all__"


class StudentDetailsFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ["name", "admission_category"]


class ParentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentDetails
        fields = "__all__"


class AcademicDetailsSerializer(serializers.ModelSerializer):
    student = StudentDetailsFilterSerializer(read_only=True)

    class Meta:
        model = AcademicDetails
        fields = ["student", "class_name", "section"]


class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentUpload
        fields = "__all__"


class StudentDetailsFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ["name", "class_name", "admission_category"]
