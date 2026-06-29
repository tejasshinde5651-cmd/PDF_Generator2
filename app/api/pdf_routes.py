# PDF routes module
import base64
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.models.health_form import ExtendedHealthCampForm, HealthCampForm
from app.services.pdf_service import PDFService
from app.utils.template_renderer import render_html

router = APIRouter()


def _load_logo_data(file_name: str) -> str:
    logo_path = Path(__file__).resolve().parent.parent / "logo" / file_name
    with logo_path.open("rb") as file:
        encoded = base64.b64encode(file.read()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


@router.post("/generate-pdf")
def generate_pdf(data: HealthCampForm):
    """Generate PDF from health camp form data"""
    
    html = render_html(
        "health_form.html",
        {
            # Header Information
            "year": data.year,
            "division": data.division,
            "logo_left": _load_logo_data("D_image.jpg"),
            "logo_right": _load_logo_data("govtofmah-DjMplB8F-removebg-preview.png"),

            # Section 1: Personal Information
            "full_name": data.full_name,
            "gender": data.gender,
            "dob": data.dob,
            "mobile": data.mobile,
            "email": data.email,
            "address": data.address,
            "pincode": data.pincode,
            "district": data.district,
            "taluka": data.taluka,
            "village": data.village,
            "aadhaar": data.aadhaar,

            # Section 2: Health Information
            "abha_available": data.abha_available,
            "abha_number": data.abha_number or "",
            "blood_group": data.blood_group or "",
            "weight": data.weight or "",
            "illness_symptoms": data.illness_symptoms or "",
            # "medication_currently": data.medication_currently,
            # "medication_details": data.medication_details or "",
            "allergy": data.allergy,
            "allergy_details": data.allergy_details or "",
            "other_details": data.other_details or "",

            # Section 3: Official Details
            "date": data.date,
            "inspection": data.inspection or "",
            "signature": data.signature or ""
        }
    )

    pdf_path = PDFService.generate_pdf(html)

    return FileResponse(
        path=pdf_path,
        media_type="application/pdf",
        filename="health_camp_form.pdf"
    )


@router.post("/generate-pdf-extended")
def generate_pdf_extended(data: ExtendedHealthCampForm):
    """Generate PDF from the extended health camp form data"""
    html = render_html(
        "health_form_extended.html",
        {
            # Header Information
            "year": data.year,
            "division": data.division,
            "logo_left": _load_logo_data("D_image.jpg"),
            "logo_right": _load_logo_data("govtofmah-DjMplB8F-removebg-preview.png"),

            # Section 1: Personal Information
            "full_name": data.full_name,
            "gender": data.gender,
            "dob": data.dob,
            "mobile": data.mobile,
            "email": data.email,
            "address": data.address,
            "pincode": data.pincode,
            "district": data.district,
            "taluka": data.taluka,
            "village": data.village,
            "aadhaar": data.aadhaar,

            # Section 2: Health Information
            "abha_available": data.abha_available,
            "abha_number": data.abha_number or "",
            "blood_group": data.blood_group or "",
            "weight": data.weight or "",
            "illness_symptoms": data.illness_symptoms or "",
            # "medication_currently": data.medication_currently,
            # "medication_details": data.medication_details or "",
            "allergy": data.allergy,
            "allergy_details": data.allergy_details or "",
            "other_details": data.other_details or "",

            # Extended fields now placed in Section 1 (personal info)
            "current_post": data.current_post or "",
            "ministry_department": data.ministry_department or "",
            "floor": data.floor or "",

            # Section 3: Official Details
            "date": data.date or "",
            "inspection": data.inspection or "",
            "signature": data.signature or ""
        }
    )

    pdf_path = PDFService.generate_pdf(html)

    return FileResponse(
        path=pdf_path,
        media_type="application/pdf",
        filename="health_camp_form_extended.pdf"
    )


