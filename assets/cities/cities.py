import pyarrow as pa
from utils import get

def process_cities():
    url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-1000/exports/csv"
    
    params = {"delimiter": ";"}
    response = get(url, params=params)
    response.raise_for_status()
    
    import pandas as pd
    from io import StringIO
    df = pd.read_csv(StringIO(response.text), sep=";", low_memory=False)
    
    cities_data = []
    for _, row in df.iterrows():
        # Parse coordinates to get latitude and longitude
        coords = row.get("coordinates", "")
        if coords and isinstance(coords, str):
            try:
                parts = coords.split(",")
                if len(parts) == 2:
                    lat = float(parts[0].strip())
                    lon = float(parts[1].strip())
                else:
                    lat, lon = None, None
            except (ValueError, AttributeError):
                lat, lon = None, None
        else:
            lat, lon = None, None
            coords = str(coords) if coords else ""
            
        cities_data.append({
            "geoname_id": row.get("geoname_id"),
            "name": str(row.get("name", "")),
            "ascii_name": str(row.get("ascii_name", "")),
            "alternate_names": str(row.get("alternate_names", "")),
            "coordinates": str(coords),
            "latitude": lat,
            "longitude": lon,
            "feature_class": str(row.get("feature_class", "")),
            "feature_code": str(row.get("feature_code", "")),
            "country_code": str(row.get("country_code", "")),
            "country_name_en": str(row.get("cou_name_en", "")),
            "admin1_code": str(row.get("admin1_code", "")),
            "admin2_code": str(row.get("admin2_code", "")),
            "admin3_code": str(row.get("admin3_code", "")),
            "admin4_code": str(row.get("admin4_code", "")),
            "population": row.get("population"),
            "elevation": row.get("elevation"),
            "digital_elevation_model": row.get("dem"),
            "timezone": str(row.get("timezone", "")),
            "modification_date": str(row.get("modification_date", ""))
        })
    
    return pa.Table.from_pylist(cities_data)