from datetime import datetime
import os
import json
from .auto_value_fields import *


frontend_path = os.path.join(os.path.dirname(__file__), "frontend.json")
template_path = os.path.join(os.path.dirname(__file__), "template.json")
cm_data_path = os.path.join(os.path.dirname(__file__), "cm_data.json")

with open(template_path, "r", encoding="utf-8") as f:
    template = json.load(f)

with open(frontend_path, "r", encoding="utf-8") as f:
    frontend = json.load(f)

with open(cm_data_path, "r", encoding="utf-8") as f:
    cm_data = json.load(f)


FORM_TEMPLATES = template
cm_json_data = cm_data


# Auto value field filling function (main helper function)
def auto_value_field(temp_template, summary=None):
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
        print(items)

        for pdf_name, field_name in items.items():
            if pdf_name in temp_template and pdf_name != "_type":
                if field_name in temp_template[pdf_name]:
                    temp_template[pdf_name][field_name] = value



    # AI GENERATED FIELDS AUTO FILLING
    for items in ai_genareted_fields:
        _type = items["_type"]
        if _type == "naretion":
            value = summary if summary else ""

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


# "VBA-21-526EZ-ARE": "are_you_claiming_no",

def check_are_you_claiming(template):
    """ 
    Check if the user is claiming 'No' and return appropriate value. 
    """
    temp_template = template.copy()
    tmp_bool = False
    for key, value in current_disability_fields.items():
        value_to_check = temp_template.get(key, {}).get(value, "")
        if value_to_check in current_disability_fields_values:
            tmp_bool = True
            break
    
    if tmp_bool:
        temp_template["VBA-21-526EZ-ARE"]["are_you_claiming_yes"] = "On"
    else:
        temp_template["VBA-21-526EZ-ARE"]["are_you_claiming_no"] = "On"
        for key, value in exposure_information_fields.items():
            temp_template[key][value] = ""

    return temp_template




def check_PTSD(template):
    """ 
    Check if the user has PTSD and return appropriate value. 
    """
    temp_template = template.copy()
    pdf_name = "VBA-21-526EZ-ARE"
    pdf_key = "do_you_have_ptsd"
    ptsd_value = temp_template.get(pdf_name, {}).get(pdf_key, "")
    
    if ptsd_value.lower() == "yes" or ptsd_value.lower() == "on":
        return True
    else:
        return False
    

def previus_claim(template):
    """ 
    Check if the user has previous claim and return appropriate value. 
    """
    temp_template = template.copy()
    pdf_name = "VBA-21-526EZ-ARE"
    pdf_key = "have_you_previously_filed_a_claim_for_va_benefits"
    previous_claim_value = temp_template.get(pdf_name, {}).get(pdf_key, "")
    
    if previous_claim_value.lower() == "yes" or previous_claim_value.lower() == "on":
        return True
    else:
        return False



# Main function to create template with values
def create_template_value_fields(frontend_data, summary=None):
    """ Create a template with values filled in based on frontend data and configuration mapping. """
    temp_template = FORM_TEMPLATES.copy()
    cm_data = cm_json_data.copy()

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

    temp_template = auto_value_field(temp_template, summary)
    final_template = check_are_you_claiming(temp_template)

    # Save the final template to a JSON file (filled_template.json)
    with open("filled_template.json", "w", encoding="utf-8") as f:
        json.dump(final_template, f, ensure_ascii=False, indent=2)
        
    return final_template


