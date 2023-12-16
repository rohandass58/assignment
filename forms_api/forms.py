from django import forms
from .models import StudentDetails, ParentDetails, AcademicDetails, DocumentUpload


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = "__all__"


class ParentDetailsForm(forms.ModelForm):
    class Meta:
        model = ParentDetails
        fields = "__all__"


class AcademicDetailsForm(forms.ModelForm):
    class Meta:
        model = AcademicDetails
        fields = "__all__"


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentUpload
        fields = "__all__"
