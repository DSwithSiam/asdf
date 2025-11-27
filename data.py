import json
import os

cm_data = {
"veterans_first_name": {
"vba-21-0781-are": "veteran_service_member_first_fname",
"vba-21-4138-are": "veteran_beneficiarys_first_fname",
"VBA-21-526EZ-ARE": "veteran_service_member_first_name",
"VBA-21-0966-ARE": "veteran_first_fname",
"vba-20-0995-are": "veteran_first_fname"
},
"veterans_middle_name": {
"vba-21-0781-are": "veteran_service_member_middle_mname",
"vba-21-4138-are": "veteran_beneficiarys_middle_mname",
"VBA-21-526EZ-ARE": "veteran_service_member_middle_name",
"VBA-21-0966-ARE": "veteran_middle_mname",
"vba-20-0995-are": "veteran_middle_mname"
},
"veterans_last_name": {
"vba-21-0781-are": "veteran_service_member_last_lname",
"vba-21-4138-are": "veteran_beneficiarys_last_lname",
"VBA-21-526EZ-ARE": "veteran_service_member_last_name",
"VBA-21-0966-ARE": "veteran_last_lname",
"vba-20-0995-are": "veteran_last_lname"
},
"veterans_ssn_part1": {
"vba-21-0781-are": "social_security_number_part1",
"vba-21-4138-are": "veteran_social_security_number_part1",
"VBA-21-526EZ-ARE": "social_security_number_part1",
"VBA-21-0966-ARE": "social_security_number_part_1",
"vba-20-0995-are": "social_security_number_part11"
},
"veterans_ssn_part2": {
"vba-21-0781-are": "social_security_number_part2",
"vba-21-4138-are": "veteran_social_security_number_part2",
"VBA-21-526EZ-ARE": "social_security_number_part2",
"VBA-21-0966-ARE": "social_security_number_part_2",
"vba-20-0995-are": "social_security_number_part12"
},
"veterans_ssn_part3": {
"vba-21-0781-are": "social_security_number_part3",
"vba-21-4138-are": "veteran_social_security_number_part3",
"VBA-21-526EZ-ARE": "social_security_number_part3",
"VBA-21-0966-ARE": "social_security_number_part_3",
"vba-20-0995-are": "social_security_number_part13"
},
"veterans_va_file_number": {
"vba-21-0781-are": "va_file_number",
"vba-21-4138-are": "va_file_number",
"VBA-21-526EZ-ARE": "va_file_number",
"VBA-21-0966-ARE": "va_file_number",
"vba-20-0995-are": "va_file_number_1"
},
"veterans_dob_month": {
"vba-21-0781-are": "dob_mmonth",
"vba-21-4138-are": "veteran_dob_month",
"VBA-21-526EZ-ARE": "dob_month",
"VBA-21-0966-ARE": "dob_month",
"vba-20-0995-are": "dob_month_1"
},
"veterans_dob_day": {
"vba-21-0781-are": "dob_dday",
"vba-21-4138-are": "veteran_dob_day",
"VBA-21-526EZ-ARE": "dob_day",
"VBA-21-0966-ARE": "dob_day",
"vba-20-0995-are": "dob_day_1"
},
"veterans_dob_year": {
"vba-21-0781-are": "dob_yyear",
"vba-21-4138-are": "veteran_dob_year",
"VBA-21-526EZ-ARE": "dob_year",
"VBA-21-0966-ARE": "dob_year",
"vba-20-0995-are": "dob_year_1"
},
"veterans_service_number": {
"vba-21-0781-are": "veteran_service_number",
"vba-21-4138-are": "veteran_service_number",
"VBA-21-526EZ-ARE": "service_number_dod_id_number",
"VBA-21-0966-ARE": "veteran_service_number",
"vba-20-0995-are": "service_number_1"
},
"veterans_telephone_area_code": {
"vba-21-0781-are": "telephone_number_area_code",
"vba-21-4138-are": "telephone_number_area_code",
"VBA-21-526EZ-ARE": "telephone_number_area_code",
"VBA-21-0966-ARE": "telephone_number_area_code",
"vba-20-0995-are": "telephone_number_area_code_1"
},
"veterans_telephone_operator_code": {
"vba-21-0781-are": "telephone_number_operator_code",
"vba-21-4138-are": "telephone_number_operator_code",
"VBA-21-526EZ-ARE": "telephone_number_operator_code",
"VBA-21-0966-ARE": "telephone_number_operator_code",
"vba-20-0995-are": "telephone_number_operator_code_1"
},
"veterans_telephone_line_number": {
"vba-21-0781-are": "telephone_line_number",
"vba-21-4138-are": "telephone_line_number",
"VBA-21-526EZ-ARE": "telephone_line_phone_number",
"VBA-21-0966-ARE": "telephone_line_number",
"vba-20-0995-are": "telephone_line_number_1"
},
"veterans_international_phone": {
"vba-21-0781-are": "international_phone_number",
"vba-21-4138-are": "international_phone_number",
"VBA-21-526EZ-ARE": "international_phone_number",
"VBA-21-0966-ARE": "international_phone_number_01",
"vba-20-0995-are": "international_phone_number_1"
},
"veterans_email_primary": {
"vba-21-0781-are": "email_address",
"vba-21-4138-are": "email_address_1",
"VBA-21-526EZ-ARE": "email_address_number_01",
"VBA-21-0966-ARE": "email_address_1",
"vba-20-0995-are": "email_address_1"
},
"veterans_mailing_address": {
"vba-21-0781-are": "",
"vba-21-4138-are": "mailing_address",
"VBA-21-526EZ-ARE": "current_mailing_address",
"VBA-21-0966-ARE": "mailing_address",
"vba-20-0995-are": "mailing_address_1"
},
"veterans_city": {
"vba-21-0781-are": "",
"vba-21-4138-are": "city",
"VBA-21-526EZ-ARE": "city_1",
"VBA-21-0966-ARE": "city",
"vba-20-0995-are": "city_1"
},
"veterans_state": {
"vba-21-0781-are": "",
"vba-21-4138-are": "state_province",
"VBA-21-526EZ-ARE": "state_province_1",
"VBA-21-0966-ARE": "state_province_1",
"vba-20-0995-are": "state_province_1"
},
"veterans_country": {
"vba-21-0781-are": "",
"vba-21-4138-are": "country",
"VBA-21-526EZ-ARE": "country_1",
"VBA-21-0966-ARE": "country",
"vba-20-0995-are": "country"
},
"veterans_zip_1": {
"vba-21-0781-are": "",
"vba-21-4138-are": "zip_code_postal_code_1",
"VBA-21-526EZ-ARE": "zip_code_postal_code_1",
"VBA-21-0966-ARE": "zip_code_postal_code_1",
"vba-20-0995-are": "zip_code_postal_code_1"
},
"veterans_zip_2": {
"vba-21-0781-are": "",
"vba-21-4138-are": "zip_code_postal_code_2",
"VBA-21-526EZ-ARE": "zip_code_postal_code_2",
"VBA-21-0966-ARE": "zip_code_postal_code_2",
"vba-20-0995-are": "zip_code_postal_code_2"
},
"veteran_signature_image": {
"vba-21-0781-are": "16a_veteran_service_members_signature",
"vba-21-4138-are": "signature_of_veteran_beneficiary_required",
"VBA-21-526EZ-ARE": "veteranservice_member_signature_required",
"VBA-21-0966-ARE": "signature_of_veteran_agent",
"vba-20-0995-are": "veteran_claimant_signature"
},
"veteran_beneficiary_signature_image": {
"vba-21-0781-are": "",
"vba-21-4138-are": "signature_of_veteran_beneficiary_required",
"VBA-21-526EZ-ARE": "",
"VBA-21-0966-ARE": "",
"vba-20-0995-are": ""
},
"consent_i_agree": {
"vba-21-0781-are": "",
"vba-21-4138-are": "",
"VBA-21-526EZ-ARE": "",
"VBA-21-0966-ARE": "I_agree_to_receive_electronic_correspondence_from_VA_in_regards_to_my_claim",
"vba-20-0995-are": ""
},
"currently_homeless_yes": {
"vba-21-0781-are": "",
"vba-21-4138-are": "",
"VBA-21-526EZ-ARE": "currently_homeless_yes",
"VBA-21-0966-ARE": "",
"vba-20-0995-are": "are_you_currently_homeless_or_at_risk_of_becoming_homeless_yes"
},
"currently_homeless_no": {
"vba-21-0781-are": "",
"vba-21-4138-are": "",
"VBA-21-526EZ-ARE": "currently_homeless_no",
"VBA-21-0966-ARE": "",
"vba-20-0995-are": "are_you_currently_homeless_or_at_risk_of_becoming_homeless_no"
},
"veterans_apt_unit": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "aptunit_number",
	"VBA-21-526EZ-ARE": "apt_unit_number_1",
	"VBA-21-0966-ARE": "aptunit_number_1",
	"vba-20-0995-are": "apt_unit_number_1"
},
"veterans_address_change_type": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "adress_changes_TEMPORARY",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_new_address": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "new_address",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": "mailing_address_2"
},
"veterans_beginning_date_month": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "beginning_date_month",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_beginning_date_day": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "beginning_date_day",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_beginning_date_year": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "beginning_date_year",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_ending_date_month": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "ending_date_month",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_ending_date_day": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "ending_date_day",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_ending_date_year": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "ending_date_year",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_release_from_active_duty_month": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "release_from_active_duty_month",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_release_from_active_duty_day": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "release_from_active_duty_day",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_release_from_active_duty_year": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "release_from_active_duty_year",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_claim_type_compensation": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "",
	"VBA-21-0966-ARE": "compensation",
	"vba-20-0995-are": ""
},
"veterans_claim_type_pension": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "",
	"VBA-21-0966-ARE": "pension",
	"vba-20-0995-are": ""
},
"veterans_claim_type_survivors": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "",
	"VBA-21-0966-ARE": "survivors",
	"vba-20-0995-are": ""
},
"veterans_payment_account_number": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "account_number",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_account_type_checking": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "account_number_checkings",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_account_type_savings": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "account_number_savings",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"veterans_routing_number": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "routing_or_transit_number",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": ""
},
"witness1_signature_image": {
	"vba-21-0781-are": "17a_signature_of_witness",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "signature_of_witness_note_only_sign_if_veteran_signed_in_item_33a_using_an_x",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": "signature_of_the_first_witness"
},
"witness1_printed_name": {
	"vba-21-0781-are": "17b_printed_name_and_address_of_witness",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "printend_name_and_addrees_of_witness_34a",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": "printed_name_first_witness"
},
"witness1_printed_address": {
	"vba-21-0781-are": "",
	"vba-21-4138-are": "",
	"VBA-21-526EZ-ARE": "",
	"VBA-21-0966-ARE": "",
	"vba-20-0995-are": "printed_address_first_witness"
}
}





FORM_TEMPLATES={

"vba-21-0781-are":
{
	"veteran_service_member_first_fname":"NoValue", # First Name
    "veteran_service_member_middle_mname":"NoValue", # Middle Name
	"veteran_service_member_last_lname":"NoValue", # Last Name
	"va_file_number":"NoValue", # VA File Number
	"veteran_service_number":"NoValue", # Service Number
	"International_Telephone_Number_If_Applicable":"NoValue", # International Telephone Number If Applicable
	"social_security_number_part1":"NoValue", # Social Security Number Part 1
	"social_security_number_part2":"NoValue", # Social Security Number Part 2
	"social_security_number_part3":"NoValue", # Social Security Number Part 3

	"dob_mmonth":"NoValue", # DOB Month
	"dob_dday":"NoValue", # DOB Day
	"dob_yyear":"NoValue",  # DOB Year
	"telephone_number_area_code":"NoValue", # Telephone Number Area Code
	"telephone_number_operator_code":"NoValue", # Telephone Number Operator Code
	"telephone_line_number":"NoValue  ", # telephone Line Number
	"international_phone_number":"NoValue", # International Phone Number
	"email_address":"NoValue", # Email Address
	"combat_tramatic_event":"On", # Combat Traumatic Event and value is On
	"personal_traumatic_event_mst_no":"On",  # Personal Traumatic Event MST No and value is On
	"personal_traumatic_event_mst_yes":"On", # Personal Traumatic Event MST Yes and value is On
	"other_traumatic_event":"On", # Other Traumatic Event and value is On
	"brief_description_of_the_traumatic_events_number_01":"NoValue",  
	"brief_description_of_the_traumatic_events_number_02":"NoValue",
	"brief_description_of_the_traumatic_events_number_03":"NoValue",
	"brief_description_of_the_traumatic_events_number_04":"NoValue",  
	"brief_description_of_the_traumatic_events_number_5":"NoValue",
	"brief_description_of_the_traumatic_events_number_6":"NoValue",
	"location_of_the_traumatic_events_number_1":"NoValue",
	"location_of_the_traumatic_events_number_2":"NoValue",
	"location_of_the_traumatic_events_number_3":"NoValue",
	"location_of_the_traumatic_events_number_4":"NoValue",
	"location_of_the_traumatic_events_number_5":"NoValue",
	"location_of_the_traumatic_events_number_6":"NoValue",

	"dates_the_traumatic_events_occured_month_number_01":"NoValue",  
	"dates_the_traumatic_events_occured_year_number_1":"NoValue",
	"dates_the_traumatic_events_occured_month_number_2":"NoValue",
	"dates_the_traumatic_events_occured_year_number_2":"NoValue",
	"dates_the_traumatic_events_occured_month_number_3":"NoValue",
	"dates_the_traumatic_events_occured_year_number_3":"NoValue",

	"dates_the_traumatic_events_occured_month_number_4":"NoValue",  
	"dates_the_traumatic_events_occured_year_number_4":"NoValue",
	"dates_the_traumatic_events_occured_month_number_5":"NoValue",
	"dates_the_traumatic_events_occured_year_number_5":"NoValue",
	"dates_the_traumatic_events_occured_month_number_6":"NoValue",
	"dates_the_traumatic_events_occured_year_number_6":"NoValue",
	

	"behavioral_changes_experienced_following_the_traumatic_event":"On",
    "behavioral_changes_experienced_following_the_traumatic_event_01": "On", # INCREASED/DECREASED USE OF LEAVE
    "behavioral_changes_experienced_following_the_traumatic_event_02": "On", # CHANGES IN PERFORMANCE OR PERFORMANCE  EVALUATIONS
    "behavioral_changes_experienced_following_the_traumatic_event_03": "On", # EPISODES OF DEPRESSION, PANIC ATTACKS, OR ANXIETY
    "behavioral_changes_experienced_following_the_traumatic_event_04": "On", # INCREASED/DECREASED USE OF PRESCRIPTION MEDICATIONS
    "behavioral_changes_experienced_following_the_traumatic_event_05": "On", # INCREASED/DECREASED USE OF OVER-THE-COUNTER MEDICATIONS
    "behavioral_changes_experienced_following_the_traumatic_event_06": "On", # INCREASED/DECREASED USE OF ALCOHOL OR DRUGS
    "behavioral_changes_experienced_following_the_traumatic_event_07": "On", # DISCIPLINARY OR LEGAL DIFFICULTIES 
    "behavioral_changes_experienced_following_the_traumatic_event_08": "On", # CHANGES IN EATING HABITS, SUCH AS OVEREATING OR UNDEREATING, OR SIGNIFICANT CHANGES IN WEIGHT
	"increased_decreased_visits_to_a_healthcare_professional_counselor_or_treatment_facility":"NoValue",     
	"request_for_a_change_in_occupational_series_or_duty_assignment":"NoValue",     
	"increased_decreased_use_of_leave":"NoValue",     
	"changes_in_performance_or_performance_evaluations":"NoValue",     
	"episodes_of_depression_panic_attacks_or_anxiety":"NoValue",     
	"increaseddecreased_use_of_prescription_medications":"NoValue",     
	"increaseddecreased_use_of_overthe_counter_medications":"NoValue",     
	"increaseddecreased_use_of_alcohol_or_drugs":"NoValue",     
	"disciplinary_or_legal_difficulties":"NoValue",     
	"changes_in_eating_habits_such_as_overeating_or_undereating_or_significant_changes_in_weight":"NoValue",     
 	"increased_decreased_visits_to_a_healthcare_professional_counselor_or_treatment_facility_checkbox":"On",     
 	"request_for_a_change_in_occupational_series_or_duty_assignment_checkbox":"On",     



	"pregnancy_tests_around_the_time_of_the_traumatic_events":"NoValue",     
	"testss_for_sexually_transmitted_infections":"NoValue",     

	"pregnancy_tests_arround_the_time_of_the_traumatic_event":"NoValue",  
	"tests_for_sexually_transmitted_infections":"NoValue",  


	"economics_or_social_behavioral_changes":"NoValue",  
	"changes_in_or_breakup_of_a_significant_relationships":"NoValue",  

	"economic_or_social_behavioral_changes":"NoValue",  
	"changes_in_or_breakup_of_a_significant_relationship":"NoValue",  


	"c_as_needed_list_any_additional_behavioral_changes_following_the_inservice_personal_traumatic_events_that_were_not_listed_in_item_10a":"NoValue", #Field Size Issue

    "was_an-official-report_field_YES": "On", 
    "was_an-official-report_field_NO": "On", 
    "was_an-official-report_field_RESTRICTED": "On",
    "was_an-official-report_field_POLICE REPORT": "On",
    "was_an-official-report_field_NEITHER": "On", 
    "was_an-official-report_field_OTHER": "On", 
    "was_an-official-report_field_UNRESTRICTED": "On", 
	"a_rape_crisis_center_or_center_for_domestic_abuse":"On",
	"a_counseling_facility_or_health_clinic":"On",
	"family_members_or_roommates":"On",
	"a_faculty_member":"On",
	"civilian_police_reports":"On",
	"medical_reports_from_civilian_physicians":"On",
	"a_chaplain_or_clergy":"On",
	"fellow_service_member":"On",
	"personal_diaries_or_journals":"On",
	"none":"On",
 	"neither":"On",

	"other_specify_below":"On",

	"have_you-received_treatment_related_to_the_impact_of_the_traumatic_event_listed_in_item-9a_01": "On", 
    "have_you-received_treatment_related_to_the_impact_of_the_traumatic_event_listed_in_item-9a_02": "On", 

	"private_helathcare_provider":"On",
	"va_vet_center":"On",
	"community_care":"On",
	"va_medical_center_and_community_based_outpatient_clinics":"On",
	"department_of_defense_military_treatment_facility":"On",
"13c_name_and_location_of_the_treatment_facility_row1":"NoValue",
"13c_name_and_location_of_the_treatment_facility_row2":"NoValue",
	
"13c_name_and_location_of_the_treatment_facility_row3":"NoValue",
"date_of_treatment_month1":"NoValue",
"date_of_treatment_year1":"NoValue",
	
"date_of_treatment_month2":"NoValue",
"date_of_treatment_year2":"NoValue",
	
"date_of_treatment_month3":"NoValue",
"date_of_treatment_year3":"NoValue",
"dont_have_date1":"On",
"dont_have_date2":"On",
"dont_have_date3":"On",

"consent_01":"On", 
"consent_02":"On",
"consent_03":"On",
"consent_04":"On",

"remarks_if_any":"NoValue",  
"16a_veteran_service_members_signature":"NoValue", #Image Field --- user_signature
"16b_date_signed_month":"CurrentMonth",
"16b_date_signed_day":"CurrentDay",
"16b_date_signed_year":"CurrentYear",
"17a_signature_of_witness":"NoValue", #Image Field
"17b_printed_name_and_address_of_witness":"NoValue",
"18a_signature_of_witness":"NoValue", #Image Field
"18b_printed_name_and_address_of_witness":"NoValue",
"alternate_signers_signature":"NoValue",
"19b_date_signed_month":"NoValue",  
"19b_date_signed_day":"NoValue",
"19b_date_signed_year":"NoValue",
"20a_poa_authorized_representatives_signature":"NoValue",
"20b_date_signed_month":"NoValue",
"19b_date_signed_day":"NoValue",  
"20b_date_signed_day":"NoValue",
"20b_date_signed_year":"NoValue",
"20c_accreditation_number":"NoValue",
"20d_date_last_submitted_month":"NoValue",
"20d_date_last_submitted_day":"NoValue",
"20d_date_last_submitted_year":"NoValue",
},



"vba-21-4138-are":
{
	"veteran_beneficiarys_first_fname":"NoValue",
	"veteran_beneficiarys_middle_mname":"NoValue",
	"veteran_beneficiarys_last_lname":"NoValue",
	"veteran_social_security_number_part1":"NoValue",
	"veteran_social_security_number_part2":"NoValue",
	"veteran_social_security_number_part3":"NoValue",
	"va_file_number":"NoValue",
	"veteran_dob_month":"NoValue",
	"veteran_dob_day":"NoValue",
	"veteran_dob_year":"NoValue",
	"veteran_service_number":"NoValue",
	"telephone_number_area_code":"NoValue",
	"telephone_number_operator_code":"NoValue",
	"telephone_line_number":"NoValue",
	"international_phone_number":"NoValue",
	"email_address_1":"NoValue",
	"email_address_2":"NoValue",
	"mailing_address":"NoValue",
	"aptunit_number":"NoValue",
	"city":"NoValue",
	"state_province":"NoValue",
	"country":"NoValue",
	"zip_code_postal_code_1":"NoValue",
	"zip_code_postal_code_2":"NoValue",
	"section_ii_remarks_the_following_statement_is_made_in_connection_with_a_claim_for_benefits_in_the_case_of_the_abovenamed_veteranbeneficiaryrow1":"NoValue",

	"veterans_social_security_part_1":"NoValue",
	"veterans_social_security_part_2":"NoValue",
	"veterans_social_security_part_3":"NoValue",
	"section_ii_remarks_continued_the_following_statement_is_made_in_connection_with_a_claim_for_benefits_in_the_case_of_the_abovenamed_veteranbeneficiaryrow1":"NoValue",
	"signature_of_veteran_beneficiary_required":"NoValue", #Image Field -- user_signature
	"date_signed_month":"CurrentMonth",
	"date_signed_day":"CurrentDay",
	"date_signed_year":"CurrentYear",
	},

    
"VBA-21-526EZ-ARE":
{
	"THE_TYPE_OF_CLAIM_PROGRAM_PROCESS_FDC_PROGRAM":"On",
	"THE_TYPE_OF_CLAIM_PROGRAM_PROCESS_IDES":"On",
	"THE_TYPE_OF_CLAIM_PROGRAM_PROCESS_STANDARD_CLAIM_PROCESS":"On",
	"THE_TYPE_OF_CLAIM_PROGRAM_PROCESS_BDD_PROGRAM_CLAIM":"On",
	"veteran_service_member_first_name":"NoValue",
	"veteran_service_member_middle_name":"NoValue",
	"veteran_service_member_last_name":"NoValue",
	"social_security_number_part1":"NoValue",
	"social_security_number_part2":"NoValue",
	"social_security_number_part3":"NoValue",
	"have_you_ever_field_a_claim_with_va_yes": "On", 
	"have_you_ever_field_a_claim_with_va_no": "On", 
	"va_file_number":"NoValue",
	"dob_month":"NoValue",
	"dob_day":"NoValue",
	"dob_year":"NoValue",
	"service_number_dod_id_number":"NoValue",
	"release_from_active_duty_month":"NoValue",
	"release_from_active_duty_day":"NoValue",
	"release_from_active_duty_year":"NoValue",
	"telephone_number_area_code":"NoValue",
	"telephone_number_operator_code":"NoValue",
	"telephone_line_phone_number":"NoValue",
	"international_phone_number":"NoValue",
	"current_mailing_address":"NoValue",
	"apt_unit_number_1":"NoValue",
	"city_1":"NoValue",
	"state_province_1":"NoValue",
	"country_1":"NoValue",
	"zip_code_postal_code_1":"NoValue",
	"zip_code_postal_code_2":"NoValue", 
 	"zip_code_postal_code":"NoValue", 
     "email_address_agree":"On", # On / Off
	"email_address_number_01":"NoValue", 
	"email_address_number_02":"NoValue",
	"12_if_you_are_currently_a_va_employee_check_the_box_includes_work_studyinternship_if_you_are_not_a_va_employee_skip_to_12_if_you_are_currently_a_va_employee_check_the_box_includes_work_studyinternship_if_you_are_not_a_va_employee_skip_to_section_ii_if_applicableii_if_applicable":"On",

	"adress_changes_TEMPORARY":"On",  
	"adress_changes_PERMANENT":"On",  
	"new_address":"NoValue",
	"apt_unit_number_2":"NoValue",
	"city_2":"On",
	"state_province_2":"NoValue",
	"country_2":"NoValue",
	"zip_code_postal_code_3":"NoValue",
	"zip_code_postal_code_4":"NoValue",
	"beginning_date_month":"NoValue",
	"beginning_date_day":"NoValue",
	"beginning_date_year":"NoValue",
	"ending_date_month":"NoValue",
	"ending_date_day":"NoValue",
	"ending_date_year":"NoValue",

	"veterans_social_security_no_1":"NoValue",
	"veterans_social_security_no_2":"NoValue",  
	"veterans_social_security_no_3":"NoValue",  
	"currently_homeless_yes" :"On", 
	"currently_homeless_no" :"On", 
	"14a_are_you_currently_homeless_if_yes_complete_item_14b_regarding_your_living_situation_yes_no":"NoValue",  
	"your_living-situation_living":"On",  
	"your_living-situation_not_currently":"On",  
	"your_living-situation_staying":"On",  
	"your_living-situation_fleeing":"On",  
	"your_living-situation_other":"On",  
	
	"other_specify":"NoValue", 
	"other_specify_2":"NoValue",  
	"risk_of_becoming_homeless_yes":"On",  
	"risk_of_becoming_homeless_no":"On",  
	"your_living-situation_2_housing":"On",  
	"your_living-situation_2_homeless":"On",  
	"your_living-situation_2_other":"On",    
	"point_of_contact":"NoValue",
	"contact_telephone_number_area_code":"NoValue",  
	"contact_telephone_number_operator_code":"NoValue",
	"contact_telephone_line_number":"NoValue",
	"enter_international_phone_number":"NoValue",
	"are_you_claiming_yes":"On",  
	"are_you_claiming_no":"On",  
	"did_you_serve_gulf_war_hazard_location_yes":"On", 
	"did_you_serve_gulf_war_hazard_location_no":"On", 
	"location_from_month":"NoValue",  
	"location_from_year":"NoValue",
	"location_to_month":"NoValue",
	"location_to_year":"NoValue",
	"herbicide_yes":"On",
	"herbicide_no":"On",
	"please_list_other_locations_where_you_served_if_not_listed_above":"NoValue",
	"location_from_month2":"NoValue",
	"location_from_year2":"NoValue",
	"location_to_month2":"NoValue",
	"location_to_year2":"NoValue",
	"been_exposed_asbestos":"On",
	"been_exposed_shad":"On",
	"been_exposed_mustard_gas":"On",
	"been_exposed_military_occupational_specialty":"On",
	"been_exposed_radiation":"On",
	"been_exposed_contaminated_water":"On",
	"been_exposed_other":"On",
	"other_specify_3":"NoValue",
	"when_were_you_exposed_from_month":"NoValue",
	"when_were_you_exposed_from_year":"NoValue",
	"when_were_you_exposed_to_month":"NoValue",
	"when_were_you_exposed_to_year":"NoValue",
	"15e_if_you_were_exposed_multiple_times_please_provide_all_additional_dates_and_locations_of_potential_exposure":"NoValue",
	"veterans_social_security_no_21":"NoValue",
	"veterans_social_security_no_22":"NoValue",
	"veterans_social_security_no_23":"NoValue",


	"current_disabilityiesrow1":"NoValue",
	"current_disabilityiesrow2":"NoValue",
	"current_disabilityiesrow3":"NoValue",
	"current_disabilityiesrow4":"NoValue",
	"current_disabilityiesrow5":"NoValue",
	"current_disabilityiesrow6":"NoValue",
	"current_disabilityiesrow7":"NoValue",
	"current_disabilityiesrow8":"NoValue",
	"current_disabilityiesrow9":"NoValue",
	"current_disabilityiesrow10":"NoValue",
	"current_disabilityiesrow11":"NoValue",
	"current_disabilityiesrow12":"NoValue",
	"current_disabilityiesrow13":"NoValue",
	"current_disabilityiesrow14":"NoValue",
	"current_disabilityiesrow15":"NoValue",
  
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow1":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow3":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow4":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow5":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow6":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow7":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow8":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow9":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow10":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow11":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow12":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow13":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow14":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow15":"NoValue",


	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow1":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow3":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow4":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow5":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow6":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow7":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow8":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow9":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow10":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow11":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow12":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow13":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow14":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow15":"NoValue",
    
	"approximate_date_disabilityies_began_or_worsenedrow1":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow3":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow4":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow5":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow6":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow7":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow8":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow9":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow10":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow11":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow12":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow13":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow14":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow15":"NoValue",



	"a_enter_the_disability_treated_and_namelocation_of_the_treatment_facilityrow1":"NoValue",
	"date_of_treatment_month_1":"NoValue",
	"date_of_treatment_year_1":"NoValue",
	"dont_have_date_1":"NoValue",
	"a_enter_the_disability_treated_and_namelocation_of_the_treatment_facilityrow2":"NoValue",
	"date_of_treatment_month_2":"NoValue",
	"date_of_treatment_year_2":"NoValue",
	"dont_have_date_2":"NoValue",
	"a_enter_the_disability_treated_and_namelocation_of_the_treatment_facilityrow3":"NoValue",
	"date_of_treatment_month_3":"NoValue",
	"date_of_treatment_year_3":"NoValue",
	"dont_have_date_3":"NoValue",

	"veterans_social_security_no_31":"NoValue",
	"veterans_social_security_no_32":"NoValue",
	"veterans_social_security_no_33":"NoValue",
  	"serve_under_another_name_yes":"On",
  	"serve_under_another_name_no":"On",
    
	"18b_list_the_other_names_you_served_under":"NoValue",
	"branch_of_service_army":"On",  
    "branch_of_service_airforce":"On",  
	"branch_of_service_noaa":"On",  
	"branch_of_service_navy":"On",  
	"branch_of_service_costguard":"On",  
	"branch_of_service_usphs":"On",  
	"branch_of_service_marinecorp":"On",  
	"branch_of_service_spaceforce":"On",  
	"19b_component_active":"On",  
	"19b_component_reserve":"On",  
	"19b_component_national_guard":"On",  


  "month_3":"NoValue",
  "day_3":"NoValue",
  "year_3":"NoValue",
  "exit_date_month":"NoValue",
  "exit_date_day":"NoValue",
  "exit_date_year":"NoValue",
  "from_month_4":"NoValue",
  "from_day_4":"NoValue",
  "from_year_4":"NoValue",
  
  
  
  "to_month_4":"NoValue",
  "to_day_4":"NoValue",
  "to_year_4":"NoValue",
  
  "the_reserves_or_national_guard_yes":"On",
  "the_reserves_or_national_guard_no":"On",
  "component_national_guard_2":"On",  
  "component_reserves_2":"On",  
  
  "from_month_5":"NoValue",  
  "from_day_5":"NoValue",  
  "from_year_5": "NoValue",
  "to_month_5":"NoValue",  
  "to_day_5":"NoValue",  
  "to_year_5":"NoValue",  
  "from_month_5":"NoValue",  



	"anticipated_separation_1":"NoValue",  
	"anticipated_separation_2":"NoValue",
	"since_9112001_yes":"On", 
	"since_9112001_no":"On", 
	"20d_from_month_4":"NoValue",  
	"20d_from_day_4":"NoValue",  
	"20d_from_year_4":"NoValue",  
	"20d_to_month_4":"NoValue",  
	"20d_to_day_4":"NoValue",  
	"20d_to_year_4":"NoValue",  
	"21a_the_reserves_or_national_guard":"On",  
	"22b_component_national_guard_2":"On",  
	"22b_component_reserves_2":"On",  
	"21c_from_month_5":"NoValue",  
	"21c_from_day_5":"NoValue", 
	"21c_from_year_5":"NoValue",  
	"21c_to_month_5":"NoValue",  
	"21c_to_day_5":"NoValue",  
	"21c_to_year_5":"NoValue",  
	"21d_current_or_last_assigned_name_and_address_of_unit":"NoValue",
	"21e_current_or_assigned_phone_number_of_unit_include_area_code":"NoValue",

	"21f_training_pay_yes":"On",
	"21f_training_pay_no":"On",

	"22a_reserves_2_yes":"On",  
	"22a_reserves_2_no":"On", 






    # Date of Activation
	"22b_month_6":"NoValue", 
  	"month_6":"NoValue", 

	"22b_day_6":"NoValue",  
 	"day_6":"NoValue",  

	"22b_year_6":"NoValue",  
 	"year_6":"NoValue",  

	# Date of Anticipated Separation
	"22c_month_7":"NoValue",  
  	"month_7":"NoValue",  

	"22c_day_7":"NoValue",	  
 	"day_7":"NoValue",	  

	"22c_year_7":"NoValue",  
 	"year_7":"NoValue",  


    "prisoner_of_war_no":"On", 
	"prisoner_of_war_yes":"On",
    
	# DATES OF CONFINEMENT 
    # From Date
	"month_8":"NoValue",
	"day_8":"NoValue",  
	"year_8":"NoValue",
    "month_10":"NoValue",  
	"day_10":"NoValue",  
	"year_10":"NoValue",  

	# To Date 
	"month_9":"NoValue",
	"day_9":"NoValue",  
	"year_9":"NoValue",	  
	"month_11": "NoValue",  
	"day_11": "NoValue",	  
	"year_11": "NoValue",	  
    

	"military_retired_pay_yes":"On", 
	"military_retired_pay_no":"On", 
    
	"military_retired_pay_in_future_yes": "On", 
	"military_retired_pay_in_future_no": "On", 
    
	"24C_branch_of_service_army":"On",  
	"24C_branch_of_service_airforce":"On",  
	"24C_branch_of_service_noaa":"On",  
	"24C_branch_of_service_navy":"On",  
	"24C_branch_of_service_navy_corps":"On",  
	"24C_branch_of_service_costguard":"On",  
	"24C_branch_of_service_usphs":"On",  
	"24C_branch_of_service_marinecorp":"On",  
	"24C_branch_of_service_space_force":"On", 
	"24D_monthly_amount_1":"NoValue",
    "24D_monthly_amount_3":"NoValue",
    
	"27C_branch_of_service_army": "On",
    "27C_branch_of_service_airforce": "On",
    "27C_branch_of_service_noaa": "On",
    "27C_branch_of_service_navy": "On",
    "27C_branch_of_service_marine_corps": "On",
    "27C_branch_of_service_costguard": "On",
    "27C_branch_of_service_usphs": "On",
    "27C_branch_of_service_marinecorps": "On",
    "27C_branch_of_service_space_force": "On",

	"retired_status_retired":"On",
	"retired_status_permanent_disability":"On",
	"retired_status_temporary_disability":"On",


	"not_pay_me_va":"On",  
	
    "veterans_social_security_no_1":"NoValue",
	"veterans_social_security_no_2":"NoValue",
	"veterans_social_security_no_3":"NoValue",
    

	"ever_received_separation_yes":"On",
	"ever_received_separation_no":"On",
  
 	"anticipated_separation_1":"NoValue",
 	"anticipated_separation_2":"NoValue",
  
	"veterans_social_security_no_41":"NoValue",
	"veterans_social_security_no_43":"NoValue",
	"veterans_social_security_no_42":"NoValue",


	"payment_received_month":"NoValue",
	"payment_received_day":"NoValue",
	"payment_received_year":"NoValue",
  
  
	"branch_of_service":"On",  
	"branch_of_service_3":"On",  
	

	# Provide pre-tax amount received
	"amount_received_1":"NoValue",  
	"amount_received_2":"NoValue",

	"not_pay_me_va_com":"On",
	"payment_agent":"On",
	"account_number":"NoValue",
	"account_number_checkings":"On",  
	"account_number_savings":"On", 
    
	"name_of_financial_institution":"NoValue",  
	"routing_or_transit_number":"NoValue",
	"veteranservice_member_signature_required":"NoFile", # Image Field -- user_signature
	"date_signed_month_33b":"CurrentMonth", 
	"date_signed_day_33b":"CurrentDay",  
	"date_signed_year_33b":"CurrentYear",
	"signature_of_witness_note_only_sign_if_veteran_signed_in_item_33a_using_an_x":"NoValue", #Image Field
	"printend_name_and_addrees_of_witness_34a":"NoValue",  		 																
	"35a_signature_of_witness_note_only_sign_if_veteran_signed_in_item_33a_using_an_x":"NoValue",# Image Field
	"printend_name_and_addrees_of_witness_35a":"NoValue",

	"veterans_social_security_no_51":"NoValue",
	"veterans_social_security_no_52":"NoValue",
	"veterans_social_security_no_53":"NoValue",
	"36a_alternate_signer_signature_required":"NoValue",
	"date_signed_month_36b":"NoValue", 
	"date_signed_day_36b":"NoValue", 	 
	"date_signed_year_36b":"NoValue",
	"37a_poaauthorized_representative_signature":"NoValue", # Image Field
	"date_signed_month_37b":"NoValue",
	"date_signed_day_37b":"NoValue",
	"date_signed_year_37b":"NoValue",

	"veterans_social_security_no_1":"NoValue", 
	"veterans_social_security_no_2":"NoValue", 
	"veterans_social_security_no_3":"NoValue", 
  
  "veterans_social_security_no_61":"NoValue", 
	"veterans_social_security_no_62":"NoValue", 
	"veterans_social_security_no_63":"NoValue", 

	"current_disability_row_1_2":"NoValue",
	"current_disability_row_2_2":"NoValue",
	"current_disability_row_3_2":"NoValue",
	"current_disability_row_4_2":"NoValue",
	"current_disability_row_5_2":"NoValue",
	"current_disability_row_6_2":"NoValue",
	"current_disability_row_7_2":"NoValue",
	"current_disability_row_8_2":"NoValue",
	"current_disability_row_9_2":"NoValue",
	"current_disability_row_10_2":"NoValue",
	"current_disability_row_11_2":"NoValue",
	"current_disability_row_12_2":"NoValue",
	"current_disability_row_13_2":"NoValue", 
	"current_disability_row_14_2":"NoValue",
	"current_disability_row_15_2":"NoValue",
	"current_disability_row_16_2":"NoValue",
	"current_disability_row_17_2":"NoValue",
	"current_disability_row_18_2":"NoValue",
	"current_disability_row_19_2":"NoValue",
	"current_disability_row_20_2":"NoValue",

	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow1_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow2_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow3_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow4_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow5_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow6_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow7_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow8_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow9_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow10_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow11_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow12_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow13_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow14_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow15_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow16_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow17_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow18_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow19_2":"NoValue",
	"if_due_to_exposure_event_or_injury_please_specify_eg_agent_orange_radiation_burn_pitsrow20_2":"NoValue",



	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow1_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow2_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow3_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow4_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow5_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow6_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow7_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow8_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow9_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow10_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow11_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow12_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow13_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow14_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow15_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow16_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow17_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow18_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow19_2":"NoValue",
	"explain_how_the_disabilityies_relates_to_the_inservice_eventexposureinjuryrow20_2":"NoValue",
	

	"approximate_date_disabilityies_began_or_worsenedrow1_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow2_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow3_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow4_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow5_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow6_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow7_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow8_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow9_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow10_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow11_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow12_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow13_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow14_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow15_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow16_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow17_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow18_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow19_2":"NoValue",
	"approximate_date_disabilityies_began_or_worsenedrow20_2":"NoValue",

},


"VBA-21-0966-ARE":
{
	"veteran_first_fname":"NoValue", 
	"veteran_middle_mname":"NoValue", 
	"veteran_last_lname":"NoValue",
	"social_security_number_part_1":"NoValue",
	"social_security_number_part_2":"NoValue",
	"social_security_number_part_3":"NoValue",
	"have_ever_filed_a_va_claim_no":"On", 
	"have_ever_filed_a_va_claim_yes":"On", 
	"va_file_number":"NoValue",
	"dob_month":"NoValue", 
	"dob_day":"NoValue",  
	"dob_year":"NoValue",  
	"veteran_service_number":"NoValue",  
	"mailing_address":"NoValue",  
	"aptunit_number_1":"NoValue",  
	"city":"NoValue",  
	"state_province_1":"NoValue",  
    "state_province_2":"NoValue",  
	"country":"NoValue",  
	"zip_code_postal_code_1":"NoValue",
	"zip_code_postal_code_2":"NoValue",    
	"telephone_number_area_code":"NoValue",
	"telephone_number_operator_code":"NoValue",
	"telephone_line_number":"NoValue",
	"international_phone_number_01":"NoValue",
	"I_agree_to_receive_electronic_correspondence_from_VA_in_regards_to_my_claim":"On",
	"email_address_1":"NoValue",
	"email_address_2":"NoValue",
	"claimants_first_name":"NoValue",
	"claimants_middle_name":"NoValue",
	"claimants_last_name":"NoValue",
	"claimant_social_security_number_part1":"NoValue",  
	"claimant_social_security_number_part2":"NoValue",  
	"claimant_social_security_number_part3":"NoValue",  
	"ever_filed_va_claim_yes":"On",  
	"ever_filed_va_claim_no":"On",  
	"claimant_va_file_number":"NoValue",  
	"relationship_to_veteran_spouse":"On", 
	"relationship_to_veteran_child":"On",  
	"relationship_to_veteran_fiduciary":"On",  
    "relationship_to_veteran_vso": "On",
	"relationship_to_veteran_service_officer":"On",  
	"relationship_to_veteran_other":"On",
	"relationship_to_veteran_alternate_signer":"On",  

	"relationship_to_veteran_third_party":"On",  

    
	"claimants_dob_month":"NoValue",  
	"claimants_dob_day":"NoValue",  
	"claimants_dob_year":"NoValue",  
	"claimant_mailing_address":"NoValue",  
	"claimant_aptunit_number":"NoValue",  
	"claimant_city":"NoValue",  
	"claimant_state_province":"NoValue",  
	"claimant_country":"NoValue",  
    "country_2":"NoValue",  
	"claimant_zip_code_postal_code_1":"NoValue",  
	"claimant_zip_code_postal_code_2":"NoValue",  
	"claimant_telephone_number_area_code":"NoValue",    
	"claimant_telephone_number_operator_code":"NoValue",    
	"claimant_telephone_line_number":"NoValue",  
	"claimant_international_phone_number":"NoValue",  
	"i_agree":"NoValue",  
	"claimant_email_address_1":"NoValue",  
	"claimant_email_address_2":"NoValue",  
    "Other_Specify":"NoValue", 

	"compensation":"On",
	"pension":"On",
	"survivors":"On",

	"signature_of_veteran_agent":"NoValue", #Image Field
	"date_signed_month":"NoValue", 
	"date_signed_day":"NoValue",
	"date_signed_year":"NoValue",
	"name_of_attorney_agent_or_veterans_service_organaization_vso_please_print":"NoValue",
	
},



"vba-20-0995-are":

{

	"benefit_type_life_insurance":"On",
	"benefit_type_fiduciary":"On",
	"benefit_type_PENSION_DIC_SURVIVORS_BENEFITS":"On",
	"benefit_type_LOAN_GUARANTY":"On",
	"benefit_type_natinal_crmetery":"On",
	"benefit_type_COMPENSATION":"On",
	"benefit_type_EDUCATION":"On",
	"benefit_type_VETERAN_READINESS_AND_EMPLOYMENT":"On",
	"benefit_type_VETERANS_HEALTH_ADMINISTRATION":"On",

    "veteran_first_fname":"NoValue",

    "veteran_middle_mname":"NoValue",

    "veteran_last_lname":"NoValue",

    "social_security_number_part11":"NoValue",

    "social_security_number_part12":"NoValue",

    "social_security_number_part13":"NoValue",

    "va_file_number_1":"NoValue",

    "dob_month_1":"NoValue",  

    "dob_day_1":"NoValue",  

    "dob_year_1":"NoValue",  

    "service_number_1":"NoValue",

    "va_insurance_policy_number_1":"NoValue",

    "mailing_address_1":"NoValue",

    "apt_unit_number_1":"NoValue",

    "city_1":"NoValue",

    "state_province_1":"NoValue",

    "country":"NoValue",

    "zip_code_postal_code_1":"NoValue",
    "zip_code_postal_code_2":"NoValue",

    "telephone_number_area_code_1":"NoValue",

    "telephone_number_operator_code_1":"NoValue",

    "telephone_line_number_1":"NoValue",

    "international_phone_number_1":"NoValue",

    "email_address_1":"NoValue",

    "email_address_2":"NoValue",

    "claimant_first_name":"NoValue",

    "claimant_middle_name":"NoValue",

    "claimant_last_name":"NoValue",

    "claimant_social_security_number_part21":"NoValue",

    "claimant_social_security_number_part22":"NoValue",

    "claimant_social_security_number_part23":"NoValue",

    "va_file_number_2":"NoValue",
    
    "dob_month_2":"NoValue",
    
    "dob_year_2":"NoValue",
    
    "dob_day_2":"NoValue",

    "claimant_dob_month":"NoValue",  

    "claimant_dob_day":"NoValue",  

    "claimant_dob_year":"NoValue",  

    "va_insurance_policy_number_2":"NoValue",

    "relationship_to_veteran_spouse":"On", 
    "relationship_to_veteran_child":"On", 
    "relationship_to_veteran_fiduciary":"On", 
    "relationship_to_veteran_parent":"On", 
    "relationship_to_veteran_other":"On", 

	"mailing_address_2":"NoValue",

    "apt_unit_number_2":"NoValue",

    "city_2":"NoValue",

    "state_province_2":"NoValue",

    "country_2":"NoValue",

    "zip_code_postal_code_3":"NoValue",

    "zip_code_postal_code_4":"NoValue",

    "telephone_number_area_code_2":"NoValue",

    "telephone_number_operator_code_2":"NoValue",

	"telephone_line_number_2":"NoValue",

    "international_phone_number_2":"NoValue",

    "email_address_3":"NoValue",

    "email_address_4":"NoValue",

	"claimant_social_security_number_part21":"NoValue", #----
    
    "claimant_social_security_number_part23":"NoValue",
    
    "claimant_social_security_number_part22":"NoValue",
    
    "email_address_1":"NoValue",
    
    
    "20a_are_you_currently_homeless_or_at_risk_of_becoming_homeless_if_yes_complete_items_20b_through_20d_regarding_your_living_situation_yes_no_if_no_skip_to_item_21":"NoValue",
    "are_you_currently_homeless_or_at_risk_of_becoming_homeless":"NoValue",
    "email_address_1":"NoValue",


    "are_you_currently_homeless_or_at_risk_of_becoming_homeless_yes":"On", 
    "are_you_currently_homeless_or_at_risk_of_becoming_homeless_no":"On", 

    "sleep":"On",

 	"shelter":"On",

	"family_member":"On",

	"next_30-days_leave_facility":"On",

	"next_30-days_lose_my_home":"On",

	"none_of_these_situations_apply_to_me":"On",

	"other_specify":"On",
    "note_va_has_access_to_vamc_cboc_and_mtf_records_a_consent_form_is_not_needed_however_if_you_would_like_va_to_attempt_to_obtain_your_private_provider":"akjsdflkajsdklfjlkasjdflj",
    
	"Statement_of_the_Case_SOC":"NoValue",
    
    "SOC_2":"NoValue",
    
    "SOC_3":"NoValue",
    
    "SOC_4":"NoValue",
    
    "SOC_5":"NoValue",
    
    "SOC_6":"NoValue",
    
    "SOC_7":"NoValue",
    
    "SOC_8":"NoValue",
    
    "SOC_9":"NoValue",
    


    "others_specify":"NoValue",

	"point_of_contact_name_of_person":"NoValue",

    "point_of_contact_telephone_number_area_code":"NoValue",

    "point_of_contact_telephone_number_operator_code":"NoValue",

    "point_of_contact_telephone_line_number":"NoValue",

    "international_phone_number_20d":"NoValue",



    "date_of_va_decision_notice_month_1":"NoValue",

    "date_of_va_decision_notice_day_1":"NoValue",

    "date_of_va_decision_notice_year_1":"NoValue",

    "date_of_va_decision_notice_month2":"NoValue",

	"date_of_va_decision_notice_day2":"NoValue",

    "date_of_va_decision_notice_year2":"NoValue",

    "date_of_va_decision_notice_month3":"NoValue",

    "date_of_va_decision_notice_day3":"NoValue",

	"date_of_va_decision_notice_year3":"NoValue",

    "date_of_va_decision_notice_month4":"NoValue",

    "date_of_va_decision_notice_day4":"NoValue",

	"date_of_va_decision_notice_year4":"NoValue",

    "date_of_va_decision_notice_month5":"NoValue",

    "date_of_va_decision_notice_day5":"NoValue",

	"date_of_va_decision_notice_year5":"NoValue",

    "date_of_va_decision_notice_month6":"NoValue",

    "date_of_va_decision_notice_day6":"NoValue",

	"date_of_va_decision_notice_year6":"NoValue",

    "date_of_va_decision_notice_month7":"NoValue",

    "date_of_va_decision_notice_day7":"NoValue",

	"date_of_va_decision_notice_year7":"NoValue",

    "date_of_va_decision_notice_month8":"NoValue",

    "date_of_va_decision_notice_day8":"NoValue",

	"date_of_va_decision_notice_year8":"NoValue",

    "date_of_va_decision_notice_month9":"NoValue",

    "date_of_va_decision_notice_day9":"NoValue",

	"date_of_va_decision_notice_year9":"NoValue",

    "private_health_care_provider_including_nonfederal_records":"On",

    "va_vet_center":"On",

	"community_care_paid_for_by_va":"On",

    "va_medical_centers_vamc_and_communitybased_outpatient_clinics_cboc":"On",

	"department_of_defense_dod_military_treatment_facilityies_mtf":"On",

    "other_specify_2":"On",
    
    
	"22b_name_and_location_of_the_treatment_facilityrow1_sn":"1",
	"22b_name_and_location_of_the_treatment_facilityrow1":"NoValue",

	"22b_name_and_location_of_the_treatment_facilityrow2_sn":"2",
    "22b_name_and_location_of_the_treatment_facilityrow2":"NoValue",

	"22b_name_and_location_of_the_treatment_facilityrow3_sn":"3",
	"22b_name_and_location_of_the_treatment_facilityrow3":"NoValue",

    "date_of_treatment_month1":"NoValue",

	"date_of_treatment_year1":"NoValue",

    "date_of_treatment_month2":"NoValue",

	"date_of_treatment_year2":"NoValue",

    "date_of_treatment_month3":"NoValue",

	"date_of_treatment_year3":"NoValue",

    "don't_have_date_1":"On",

	"don't_have_date_2":"On",

	"don't_have_date_3":"On",

	"i_certify_that_yes":"On",
	"i_certify_that_no":"Off",

	"i_consent":"On",
	"i_donot_consent":"On",
	"revoke_consent":"On",
	"not_applicable_consent":"On",

	"veteran_claimant_signature":"Image Field", # Image Field user_signature

	"25b_date_signed_month":"CurrentMonth",

    "25b_date_signed_day":"CurrentDay",

    "25b_date_signed_year":"CurrentYear",

	"signature_of_the_first_witness":"NoValue",

    "printed_name_first_witness":"NoValue",

    "printed_address_first_witness":"NoValue",

	"signature_of_the_second_witness":"NoValue",

    "printed_name_second_witness":"NoValue",

    "printed_address_second_witness":"NoValue",

	"alternate_signer_signature":"NoValue",

	"28b_date_signed_month":"NoValue",

    "28b_date_signed_day":"NoValue",

    "28b_date_signed_year":"NoValue",

	"poa_authorized_representative_signature":"NoValue",

    "29b_date_signed_month":"NoValue",

    "29b_date_signed_day":"NoValue",

	"29b_date_signed_year":"NoValue",

    "accreditation_number":"NoValue",

    "date_last_va_from_21_22_month":"NoValue",

	"date_last_va_from_21_22_day":"NoValue",

	"date_last_va_from_21_22_year":"NoValue",

}
}





json_path = os.path.join(os.path.dirname(__file__), "cm_data.json")
key_list_path = os.path.join(os.path.dirname(__file__), "key_list.json")

# load existing cm_data if present
if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        cm_data = json.load(f)
else:
    cm_data = {}

# load existing key list (if any) and treat those keys as already present
existing_key_list = set()
if os.path.exists(key_list_path):
    try:
        with open(key_list_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                existing_key_list = set(data)
    except Exception:
        existing_key_list = set()

missing = set()
for form_name, template in FORM_TEMPLATES.items():
    for pdf_name in template.keys():
        # do not add if key already exists in cm_data or in existing key_list
        if pdf_name not in cm_data and pdf_name not in existing_key_list:
            missing.add(pdf_name)

if missing:
    for pdf_name in sorted(missing):
        cm_data[pdf_name] = {
            form: (pdf_name if pdf_name in FORM_TEMPLATES[form] else "")
            for form in FORM_TEMPLATES
        }
        for pdf_name in sorted(missing):
            cm_data[pdf_name] = {
            form: (pdf_name if pdf_name in FORM_TEMPLATES[form] else "")
            for form in FORM_TEMPLATES
            }
            # overall field type: "checkbox" if any form marks it as "On", otherwise "str"
            overall_type = "checkbox" if any(
            FORM_TEMPLATES[form].get(pdf_name) == "On" for form in FORM_TEMPLATES
            ) else "str"
            cm_data[pdf_name]["_types"] = overall_type

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cm_data, f, indent=2, ensure_ascii=False)


# def write_cm_value_lists_to_json(json_path: str | None = None) -> list[str]:
#     """
#     Collect all non-empty, unique cm_data values (preserving first-seen order)
#     and write them as a JSON array. Returns the list written.
#     """
#     if json_path is None:
#         json_path = os.path.join(os.path.dirname(__file__), "key_list.json")

#     values_list: list[str] = []
#     seen: set[str] = set()

#     if isinstance(cm_data, dict):
#         for form_map in cm_data.values():
#             if isinstance(form_map, dict):
#                 for v in form_map.values():
#                     if v and isinstance(v, str) and v not in seen:
#                         values_list.append(v)
#                         seen.add(v)

#     dirpath = os.path.dirname(json_path) or os.path.dirname(__file__)
#     os.makedirs(dirpath, exist_ok=True)
#     with open(json_path, "w", encoding="utf-8") as f:
#         json.dump(values_list, f, indent=2, ensure_ascii=False)

#     return values_list


# if __name__ == "__main__":
#     values = write_cm_value_lists_to_json()
#     print(f"Wrote {len(values)} unique values to {os.path.join(os.path.dirname(__file__), 'key_list.json')}")
