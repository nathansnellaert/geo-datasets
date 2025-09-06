import pyarrow as pa
from utils import get

def process_organizations():
    url = "https://raw.githubusercontent.com/dieghernan/Country-Codes-and-International-Organizations/master/outputs/CountrycodesOrgs.csv"
    
    response = get(url)
    response.raise_for_status()
    
    import pandas as pd
    from io import StringIO
    df = pd.read_csv(StringIO(response.text))
    
    orgs_data = []
    for _, row in df.iterrows():
        orgs_data.append({
            "name": row.get("NAME", ""),
            "iso3": row.get("ISO3", ""),
            "iso2": row.get("ISO2", ""),
            "un_member": row.get("UN_MEMBER") == 1,
            "world_bank": row.get("World_Bank") == 1,
            "imf": row.get("IMF") == 1,
            "oecd": row.get("OECD") == 1,
            "brics": row.get("BRICS") == 1,
            "g7": row.get("G7") == 1,
            "g20": row.get("G20") == 1,
            "eu": row.get("EU") == 1,
            "eurozone": row.get("Eurozone") == 1,
            "schengen": row.get("Schengen") == 1,
            "nato": row.get("NATO") == 1,
            "commonwealth": row.get("Commonwealth") == 1,
            "asean": row.get("ASEAN") == 1,
            "apec": row.get("APEC") == 1,
            "mercosur": row.get("Mercosur") == 1,
            "opec": row.get("OPEC") == 1,
            "african_union": row.get("AU") == 1,
            "arab_league": row.get("Arab_League") == 1
        })
    
    return pa.Table.from_pylist(orgs_data)