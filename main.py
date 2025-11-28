import os
import json
from typing import Any, Dict, List

from auto_data_field import auto_value_field, auto_value_field
json_path = os.path.join(os.path.dirname(__file__), "cm_data.json")
# load existing cm_data if present
if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        cm_data = json.load(f)
else:
    cm_data = {}


# # print(cm_data)
# for key in cm_data:
#     frontend_path = os.path.join(os.path.dirname(__file__), "frontend.json")
#     # load existing list of keys
#     if os.path.exists(frontend_path):
#         with open(frontend_path, "r", encoding="utf-8") as f:
#             try:
#                 frontend = json.load(f)
#                 if not isinstance(frontend, dict):
#                     frontend = {}
#             except Exception:
#                 frontend = {}
#     else:
#         frontend = {}

#     if key not in frontend:
#         entry = cm_data.get(key, {})
#         if not isinstance(entry, dict):
#             entry = {}
#         _types = entry.get("_types", "")
#         if _types == "str":  
#             value = "1234"
#         elif _types == "checkbox":
#             value = "On"
#         elif _types == "signature":
#             value = ""
#         else:
#             value = ""
#         frontend[key] = value
#         with open(frontend_path, "w", encoding="utf-8") as f:
#             json.dump(frontend, f, ensure_ascii=False, indent=2)




frontend_path = os.path.join(os.path.dirname(__file__), "frontend.json")
template_path = os.path.join(os.path.dirname(__file__), "template.json")

with open(template_path, "r", encoding="utf-8") as f:
    template = json.load(f)

frontend = {}
try:
    if os.path.exists(frontend_path):
        with open(frontend_path, "r", encoding="utf-8") as f:
            frontend = json.load(f)
            if not isinstance(frontend, dict):
                frontend = {}
    else:
        frontend = {}
except Exception:
    frontend = {}



def checkbox_value_formating(value):
    if value in [True, "true", "True", "on", "On"]:
        return "On"
    else:
        return ""


        

def create_template_value_fields(demo_template, frontend_data, cm_data):
    temp_template = demo_template.copy()

    for key, value in frontend_data.items():
        if key in cm_data.keys():
            entry = cm_data.get(key, {})
            if not isinstance(entry, dict):
                entry = {}
            _types = entry.get("_types", "str")
            
            for pdf_number, pdf_field in entry.items():
                # skip the special _types entry which is not a PDF field mapping
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
    return final_template



new_template = create_template_value_fields(demo_template = template, frontend_data = frontend, cm_data = cm_data)

with open("filled_template.json", "w", encoding="utf-8") as f:
    json.dump(new_template, f, ensure_ascii=False, indent=2)