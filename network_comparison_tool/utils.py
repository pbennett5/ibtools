# utils.py
import pandas as pd

def identify_insurance_company(headers):
    cigna_headers = ['COUNTRY', 'REGION', 'SUBREGION', 'TYPE', 'PROVIDER', 'BUILDING ADDRESS', 'LICENSE NUMBER', 'SPECIAL NOTES', 'POBOX', 'PROVIDER_STARTDATE', 'TELEPHONE', 'FAX', 'HAS DENTAL SERVICE', 'Provider Group', 'Open Network 1', 'Open Network 2', 'Open Network 3']
    nextcare_headers = ['Country', 'City', 'Type', 'Category', 'Name', 'Area', 'POB', 'Address', 'Tel', 'Fax', 'Remarks', 'Code', '


# utils.py
from .models import Provider

def import_data_to_db(df, insurance_company):
    mappings = {
        'cigna': {
            'country': 'COUNTRY',
            'region': 'REGION',
            'subregion': 'SUBREGION',
            'type': 'TYPE',
            'provider': 'PROVIDER',
            # Add the remaining mappings for Cigna
        },
        'nextcare': {
            'country': 'Country',
            'city': 'City',
            'type': 'Type',
            # Add the remaining mappings for Nextcare
        },
        'sukoon': {
            'provider_name': 'Provider Name',
            'type': 'Type',
            'address': 'Address',
            # Add the remaining mappings for Sukoon
        }
    }

    for _, row in df.iterrows():
        provider_data = {field: row[mappings[insurance_company][field]] for field in mappings[insurance_company]}
        provider = Provider(**provider_data)
        provider.save()
