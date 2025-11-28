import os
import json
from typing import Any, Dict, List
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
#                 if not isinstance(frontend, list):
#                     frontend = []
#             except Exception:
#                 frontend = []
#     else:
#         frontend = []

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
#         frontend.append({key: value})
#         with open(frontend_path, "w", encoding="utf-8") as f:
#             json.dump(frontend, f, ensure_ascii=False, indent=2)



def load_json(path: str) -> Any:
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: str, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def frontend_list_to_map(frontend: Any) -> Dict[str, Any]:
    # frontend expected to be a list of single-key dicts like [{"field1": "val"}, {"field2": "val2"}]
    result: Dict[str, Any] = {}
    if isinstance(frontend, dict):
        return frontend.copy()
    if not isinstance(frontend, list):
        return result
    for item in frontend:
        if isinstance(item, dict):
            for k, v in item.items():
                result[k] = v
    return result

def apply_values_to_template(template: Any, values: Dict[str, Any]) -> Any:
    # Try several common template shapes:
    # 1) template["fields"] is a list of field objects with "name"/"key"/"id" -> set "value"
    # 2) template["fields"] is a dict keyed by field name -> set sub-dict["value"] or value
    # 3) top-level keys of template map directly to field names
    if template is None:
        return None

    # Case 1: fields as list
    fields = template.get("fields") if isinstance(template, dict) else None
    if isinstance(fields, list):
        for fld in fields:
            if not isinstance(fld, dict):
                continue
            # identify the field name/key
            field_key = fld.get("name") or fld.get("key") or fld.get("id")
            if field_key and field_key in values:
                fld["value"] = values[field_key]
        return template

    # Case 2: fields as dict
    if isinstance(fields, dict):
        for k, v in values.items():
            if k in fields:
                target = fields[k]
                if isinstance(target, dict):
                    target["value"] = v
                else:
                    fields[k] = v
        template["fields"] = fields
        return template

    # Case 3: top-level keys
    if isinstance(template, dict):
        for k, v in values.items():
            if k in template:
                if isinstance(template[k], dict):
                    template[k]["value"] = v
                else:
                    template[k] = v
            else:
                # create new entry for unknown keys
                template[k] = v
        return template

    # Fallback: return unmodified
    return template

# Entrypoint: read frontend.json and template.json, apply values, save to template_data.json
base_dir = os.path.dirname(__file__)
frontend_path = os.path.join(base_dir, "frontend.json")
template_path = os.path.join(base_dir, "template.json")
out_path = os.path.join(base_dir, "template_data.json")

frontend = load_json(frontend_path) or []
template = load_json(template_path) or {}

values_map = frontend_list_to_map(frontend)
new_template = apply_values_to_template(template, values_map)

save_json(out_path, new_template)