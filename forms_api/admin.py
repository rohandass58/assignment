from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from forms_api.models import (
    StudentDetails,
    ParentDetails,
    AcademicDetails,
    DocumentUpload,
)


class StudentDetailsResource(resources.ModelResource):
    class Meta:
        model = StudentDetails


class ParentDetailsResource(resources.ModelResource):
    class Meta:
        model = ParentDetails


class AcademicDetailsResource(resources.ModelResource):
    class Meta:
        model = AcademicDetails


class DocumentUploadResource(resources.ModelResource):
    class Meta:
        model = DocumentUpload


class StudentDetailsAdmin(ImportExportModelAdmin):
    resource_classes = [StudentDetailsResource]


class ParentDetailsAdmin(ImportExportModelAdmin):
    resource_classes = [ParentDetailsResource]


class AcademicDetailsAdmin(ImportExportModelAdmin):
    resource_classes = [AcademicDetailsResource]


class DocumentUploadAdmin(ImportExportModelAdmin):
    resource_classes = [DocumentUploadResource]


admin.site.register(StudentDetails, StudentDetailsAdmin)
admin.site.register(ParentDetails, ParentDetailsAdmin)
admin.site.register(AcademicDetails, AcademicDetailsAdmin)
admin.site.register(DocumentUpload, DocumentUploadAdmin)
