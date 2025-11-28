import os
import json
json_path = os.path.join(os.path.dirname(__file__), "cm_data.json")
# load existing cm_data if present
if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        cm_data = json.load(f)
else:
    cm_data = {}


# print(cm_data)
for key in cm_data:
    frontend_path = os.path.join(os.path.dirname(__file__), "frontend.json")
    # load existing list of keys
    if os.path.exists(frontend_path):
        with open(frontend_path, "r", encoding="utf-8") as f:
            try:
                frontend = json.load(f)
                if not isinstance(frontend, list):
                    frontend = []
            except Exception:
                frontend = []
    else:
        frontend = []

    if key not in frontend:
        frontend.append(key)
        with open(frontend_path, "w", encoding="utf-8") as f:
            json.dump(frontend, f, ensure_ascii=False, indent=2)