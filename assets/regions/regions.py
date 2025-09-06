import pyarrow as pa
from utils import get

def process_regions():
    url = 'https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv'
    
    response = get(url)
    response.raise_for_status()
    
    import pandas as pd
    from io import StringIO
    df = pd.read_csv(StringIO(response.text), keep_default_na=False)
    
    regions_set = set()
    
    for _, row in df.iterrows():
        region = row.get("Region Name", "")
        sub_region = row.get("Sub-region Name", "")
        intermediate = row.get("Intermediate Region Name", "")
        
        if region or sub_region or intermediate:
            regions_set.add((region, sub_region, intermediate))
    
    regions_data = []
    for region, sub_region, intermediate in regions_set:
        if region or sub_region or intermediate:
            regions_data.append({
                "region_name": region if region else None,
                "sub_region_name": sub_region if sub_region else None,
                "intermediate_region_name": intermediate if intermediate else None
            })
    
    return pa.Table.from_pylist(regions_data)