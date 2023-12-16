# from django.urls import path
# from .views import (
#     StudentDetailsCreateView,
#     ParentDetailsCreateView,
#     AcademicDetailsCreateView,
#     DocumentUploadCreateView,
# )
# from . import views

# urlpatterns = [
#     path("", views.HomeView.as_view(), name="home"),
#     path("student-form/", StudentDetailsCreateView.as_view(), name="student_form"),
#     path("parent-form/", ParentDetailsCreateView.as_view(), name="parent_form"),
#     path("academic-form/", AcademicDetailsCreateView.as_view(), name="academic_form"),
#     path("document-form/", DocumentUploadCreateView.as_view(), name="document_form"),
#     path("display-data/", views.DisplayDataView.as_view(), name="display_data"),
#     path("export_to_excel/", views.ExportToExcelView.as_view(), name="export_to_excel"),
#     path("export/pdf/", views.ExportToPDFView.as_view(), name="export-pdf"),
# ]

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentDetailsViewSet,
    ParentDetailsViewSet,
    AcademicDetailsViewSet,
    DocumentUploadViewSet,
    AcademicDetailsViewSet,
    Display_data,
    student_details_form,
    student_academic_detail,
    Home,
)
from . import views

router = DefaultRouter()
router.register(r"student-details", StudentDetailsViewSet)
router.register(r"parent-details", ParentDetailsViewSet)
router.register(r"document-upload", DocumentUploadViewSet)
router.register(
    r"academic-details", AcademicDetailsViewSet, basename="academic-details"
)


urlpatterns = [
    path("display-data/", Display_data.as_view(), name="display_data"),
    path("api/", include(router.urls)),
    path("student-details-form/", student_details_form, name="student_details_form"),
    path(
        "student-academic-form/<int:pk>",
        student_academic_detail,
        name="student_academic_form",
    ),
    path("", Home.as_view(), name="home"),
]
