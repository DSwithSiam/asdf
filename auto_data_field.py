from datetime import datetime


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
   
    "_type": "naretion"
    }
]



def auto_value_field(temp_template):
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