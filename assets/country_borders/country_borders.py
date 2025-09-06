import pyarrow as pa
from utils import get

def process_country_borders():
    url = "https://raw.githubusercontent.com/geodatasource/country-borders/master/GEODATASOURCE-COUNTRY-BORDERS.CSV"
    
    response = get(url)
    response.raise_for_status()
    
    import pandas as pd
    from io import StringIO
    df = pd.read_csv(StringIO(response.text), keep_default_na=False)
    
    borders_data = []
    for _, row in df.iterrows():
        borders_data.append({
            "country_code": row.get("country_code", ""),
            "country_name": row.get("country_name", ""),
            "country_border_code": row.get("country_border_code", ""),
            "country_border_name": row.get("country_border_name", "")
        })
    
    return pa.Table.from_pylist(borders_data)