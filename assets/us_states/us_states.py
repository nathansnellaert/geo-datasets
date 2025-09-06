import pyarrow as pa
from utils import get

def process_us_states():
    url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-united-states-of-america-state/exports/csv"
    
    params = {"delimiter": ";"}
    response = get(url, params=params)
    response.raise_for_status()
    
    import pandas as pd
    from io import StringIO
    df = pd.read_csv(StringIO(response.text), sep=";")
    
    states_data = []
    for _, row in df.iterrows():
        states_data.append({
            "state_code": row.get("ste_code", ""),
            "state_name": row.get("ste_name", ""),
            "state_label": row.get("ste_label_en", ""),
            "iso3166_2": row.get("ste_iso3166_2", ""),
            "area_code": row.get("ste_area_code", ""),
            "type": row.get("ste_type", ""),
            "capital": row.get("ste_capital", ""),
            "latitude": row.get("geo_point_2d", "").split(",")[0] if pd.notna(row.get("geo_point_2d")) and "," in str(row.get("geo_point_2d")) else None,
            "longitude": row.get("geo_point_2d", "").split(",")[1] if pd.notna(row.get("geo_point_2d")) and "," in str(row.get("geo_point_2d")) else None,
            "year": row.get("year"),
            "geo_shape": row.get("geo_shape", ""),
            "bbox": row.get("ste_bbox", "")
        })
    
    return pa.Table.from_pylist(states_data)