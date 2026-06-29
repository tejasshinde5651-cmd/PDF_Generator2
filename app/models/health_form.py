# Health form model
from pydantic import BaseModel
from typing import Optional


class HealthCampForm(BaseModel):
    # Header Information
    year: str = "२०२६"
    division: str = "धारासिव"

    # Section 1: Personal Information (बैयक्तिक माहिती)
    full_name: str
    gender: str
    dob: str
    mobile: str
    email: str
    address: str
    pincode: str
    district: str
    taluka: str
    village: str
    aadhaar: str

    # Section 2: Health Information (आरोग्यावैज्ञानिक माहिती)
    abha_available: bool = False
    abha_number: Optional[str] = None
    blood_group: Optional[str] = None
    weight: Optional[str] = None
    illness_symptoms: Optional[str] = None
    # medication_currently: bool = False
    # medication_details: Optional[str] = None
    allergy: bool = False
    allergy_details: Optional[str] = None
    other_details: Optional[str] = None

    # Section 3: Official Details (कार्यलयीन तपशील)
    date: str
    inspection: Optional[str] = None
    signature: Optional[str] = None


class ExtendedHealthCampForm(HealthCampForm):
    # Additional fields for the new form variant
    # 'current_post' corresponds to 'सध्याचे पद' shown in the attachment
    current_post: Optional[str] = None
    ministry_department: Optional[str] = None
    floor: Optional[str] = None