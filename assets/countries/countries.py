import pyarrow as pa
from utils import get

def process_countries():
    url = 'https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv'
    
    response = get(url)
    response.raise_for_status()
    
    import pandas as pd
    from io import StringIO
    df = pd.read_csv(StringIO(response.text), keep_default_na=False)
    
    countries_data = []
    for _, row in df.iterrows():
        countries_data.append({
            "name": row.get("CLDR display name", ""),
            "official_name_en": row.get("official_name_en", ""),
            "official_name_fr": row.get("official_name_fr", ""),
            "iso3166_1_alpha_2": row.get("ISO3166-1-Alpha-2", ""),
            "iso3166_1_alpha_3": row.get("ISO3166-1-Alpha-3", ""),
            "iso3166_1_numeric": row.get("ISO3166-1-numeric", ""),
            "iso4217_currency_alphabetic_code": row.get("ISO4217-currency_alphabetic_code", ""),
            "iso4217_currency_country_name": row.get("ISO4217-currency_country_name", ""),
            "m49": row.get("M49", ""),
            "region_code": row.get("Region Code", ""),
            "sub_region_code": row.get("Sub-region Code", ""),
            "intermediate_region_code": row.get("Intermediate Region Code", ""),
            "region_name": row.get("Region Name", ""),
            "sub_region_name": row.get("Sub-region Name", ""),
            "intermediate_region_name": row.get("Intermediate Region Name", ""),
            "continent": row.get("Continent", ""),
            "capital": row.get("Capital", ""),
            "developed_developing_countries": row.get("Developed / Developing Countries", ""),
            "land_locked_developing_countries_lldc": row.get("Land Locked Developing Countries (LLDC)", "") == "x",
            "least_developed_countries_ldc": row.get("Least Developed Countries (LDC)", "") == "x",
            "small_island_developing_states_sids": row.get("Small Island Developing States (SIDS)", "") == "x",
            "languages": row.get("Languages", ""),
            "geoname_id": row.get("Geoname ID", ""),
            "edgar": row.get("EDGAR", "")
        })
    
    return pa.Table.from_pylist(countries_data)