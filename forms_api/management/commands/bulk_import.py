import csv
from django.core.management.base import BaseCommand
from forms_api.models import (
    StudentDetails,
    ParentDetails,
    AcademicDetails,
    DocumentUpload,
)


class Command(BaseCommand):
    help = "Bulk import data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]

        try:
            with open(csv_file_path, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    student_data = {
                        "name": row["Name"],
                        "gender": row["Gender"],
                        "adhar_card_number": row["Adhar Card Number"],
                        "dob": row["DOB"],
                        "identification_marks": row["Identification Marks"],
                        "admission_category": row["Admission Category"],
                        "height": row["Height"],
                        "weight": row["Weight"],
                        "mail_id": row["Mail Id"],
                        "contact_detail": row["Contact Detail"],
                        "address": row["Address"],
                    }
                    student = StudentDetails.objects.create(**student_data)

                    parent_data = {
                        "father_name": row["Father’s Name"],
                        "father_qualification": row["Father’s Qualification"],
                        "father_profession": row["Father’s Profession"],
                        "father_designation": row["Father’s Designation"],
                        "father_aadhar_card": row["Father’s Aadhar Card"],
                        "father_mobile_number": row["Father’s Mobile Number"],
                        "father_mail_id": row["Father’s Mail Id"],
                        "mother_name": row["Mother’s Name"],
                        "mother_qualification": row["Mother’s Qualification"],
                        "mother_profession": row["Mother’s Profession"],
                        "mother_designation": row["Mother’s Designation"],
                        "mother_aadhar_card": row["Mother’s Aadhar Card"],
                        "mother_mobile_number": row["Mother’s Mobile Number"],
                        "mother_mail_id": row["Mother’s Mail Id"],
                    }
                    parent = ParentDetails.objects.create(**parent_data)

                    academic_data = {
                        "enrollment_id": row["Enrollment ID"],
                        "class_name": row["Class"],
                        "section": row["Section"],
                        "date_of_joining": row["DOJ"],
                    }
                    academic = AcademicDetails.objects.create(**academic_data)

                    document_data = {
                        "student": student,
                        "document": row["Document"],
                    }
                    document = DocumentUpload.objects.create(**document_data)

            self.stdout.write(self.style.SUCCESS("Data imported successfully"))

        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f"File not found at path: {csv_file_path}")
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error during import: {str(e)}"))
