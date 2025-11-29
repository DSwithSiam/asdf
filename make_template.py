import os
import json

frontend_path = os.path.join(os.path.dirname(__file__), "frontend.json")
template_path = os.path.join(os.path.dirname(__file__), "template.json")
cm_data_path = os.path.join(os.path.dirname(__file__), "cm_data.json")

with open(template_path, "r", encoding="utf-8") as f:
    template = json.load(f)

with open(frontend_path, "r", encoding="utf-8") as f:
    frontend = json.load(f)

with open(cm_data_path, "r", encoding="utf-8") as f:
    cm_data = json.load(f)



# --------------------------- Auto Data Field Module ---------------------------

from datetime import datetime
import json


signecher_date_fields = [
    {
    "VBA-21-526EZ-ARE" : "date_signed_month_33b",
    "vba-21-4138-are" : "date_signed_month",
    "VBA-21-0966-AREvba-21-0781-are" : "date_signed_month",
    "vba-20-0995-are" : "25b_date_signed_month",
    "vba-21-0781-are" : "16b_date_signed_month",
    "_type": "month"
    },
    
    { 
    "VBA-21-526EZ-ARE" : "date_signed_day_33b",
    "vba-21-4138-are" : "date_signed_day",
    "VBA-21-0966-ARE" : "date_signed_day",
    "vba-20-0995-are" : "25b_date_signed_day",
    "vba-21-0781-are" : "16b_date_signed_day",
    "_type": "day"
    },

    {
    "VBA-21-526EZ-ARE" : "date_signed_year_33b",
    "vba-21-4138-are" : "date_signed_year",
    "VBA-21-0966-ARE" : "date_signed_year",
    "vba-20-0995-are" : "25b_date_signed_year",
    "vba-21-0781-are" : "16b_date_signed_year",
    "_type": "year"
    }
]    


ai_genareted_fields = [
    {
    "vba-21-4138-are" : "section_ii_remarks_the_following_statement_is_made_in_connection_with_a_claim_for_benefits_in_the_case_of_the_abovenamed_veteranbeneficiaryrow1",
    "vba-21-4138-are": "section_ii_remarks_continued_the_following_statement_is_made_in_connection_with_a_claim_for_benefits_in_the_case_of_the_abovenamed_veteranbeneficiaryrow1",
    "_type": "naretion"
    }
]

static_fields = [
    {
    "VBA-21-526EZ-ARE" : "THE_TYPE_OF_CLAIM_PROGRAM_PROCESS_FDC_PROGRAM",
    "VBA-21-526EZ-ARE": "email_address_agree",
    "VBA-21-526EZ-ARE": "are_you_claiming_no",
    "VBA-21-0966-ARE":"I_agree_to_receive_electronic_correspondence_from_VA_in_regards_to_my_claim",
    "VBA-21-0966-ARE": "compensation",
    "vba-21-0781-are": "consent_04",
    "vba-20-0995-are": "benefit_type_COMPENSATION",
    "vba-20-0995-are":"i_certify_that_yes",
    "vba-20-0995-are":"not_applicable_consent",

    "_type": "checkbox"
    },
    {
    "VBA-21-526EZ-ARE" : "name_of_financial_institution",
    "_value": "Already Established",
    "_type": "str"
    }
]


signecher_fields = {
    "VBA-21-526EZ-ARE" : "veteranservice_member_signature_required",
    "vba-21-0781-are" : "16a_veteran_service_members_signature",
    "vba-21-4138-are":"signature_of_veteran_beneficiary_required",
    "VBA-21-0966-ARE":"signature_of_veteran_agent",
    "vba-20-0995-are":"veteran_claimant_signature",
    }




# Auto value field filling function (main helper function)
def auto_value_field(temp_template):
    """ Auto fill certain fields with predefined values like current date etc. """

    datetime_now = datetime.now()
    # SIGNED DATE AUTO FILLING
    for items in signecher_date_fields:
        _type = items["_type"]
        if _type == "day":
            value = str(datetime_now.day)
        elif _type == "month":
            value = str(datetime_now.month)
        elif _type == "year":
            value = str(datetime_now.year)

        items.pop("_type", None)

        for pdf_name, field_name in items.items():
            if pdf_name in temp_template:
                if field_name in temp_template[pdf_name]:
                    temp_template[pdf_name][field_name] = value



    # AI GENERATED FIELDS AUTO FILLING
    for items in ai_genareted_fields:
        _type = items["_type"]
        if _type == "naretion":
            value = "This section to be filled by AI generated content."

        items.pop("_type", None)

        for pdf_name, field_name in items.items():
            if pdf_name in temp_template:
                if field_name in temp_template[pdf_name]:
                    temp_template[pdf_name][field_name] = value


    return temp_template


# Checkbox value formatting (main helper function)
def checkbox_value_formating(value):
    """ Format checkbox value to "On" or "" based on input. """
    if value in [True, "true", "True", "on", "On"]:
        return "On"
    else:
        return ""


        
# Main function to create template with values
def create_template_value_fields(demo_template, frontend_data, cm_data):
    """ Create a template with values filled in based on frontend data and configuration mapping. """
    temp_template = demo_template.copy()

    for key, value in frontend_data.items():
        if key in cm_data.keys():
            entry = cm_data.get(key, {})
            if not isinstance(entry, dict):
                entry = {}
            _types = entry.get("_types", "str")
            
            for pdf_number, pdf_field in entry.items():
                if pdf_number == "_types":
                    continue

                # ensure the target page/dict exists
                if pdf_number not in temp_template or not isinstance(temp_template[pdf_number], dict):
                    temp_template[pdf_number] = {}

                if _types == "str":
                    temp_template[pdf_number][pdf_field] = value
                
                elif _types == "checkbox":
                    # Apply value filtering
                    checkbox_value = checkbox_value_formating(value)
                    temp_template[pdf_number][pdf_field] = checkbox_value
                
                elif _types == "signature":
                    temp_template[pdf_number][pdf_field] = ""
                else:
                    temp_template[pdf_number][pdf_field] = ""

    final_template = auto_value_field(temp_template)

    # Save the final template to a JSON file (filled_template.json)
    with open("filled_template.json", "w", encoding="utf-8") as f:
        json.dump(final_template, f, ensure_ascii=False, indent=2)
        
    return final_template



new_template = create_template_value_fields(demo_template = template, frontend_data = frontend, cm_data = cm_data)