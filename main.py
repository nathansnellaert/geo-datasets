import os
os.environ['CONNECTOR_NAME'] = 'geo-datasets'
os.environ['RUN_ID'] = os.getenv('RUN_ID', 'local-run')

from utils import validate_environment, upload_data
from assets.countries.countries import process_countries
from assets.cities.cities import process_cities
from assets.us_states.us_states import process_us_states
from assets.country_borders.country_borders import process_country_borders
from assets.regions.regions import process_regions
from assets.organizations.organizations import process_organizations

def main():
    validate_environment()
    
    countries_data = process_countries()
    regions_data = process_regions()
    cities_data = process_cities()
    us_states_data = process_us_states()
    country_borders_data = process_country_borders()
    organizations_data = process_organizations()
    
    upload_data(countries_data, "countries")
    upload_data(regions_data, "regions")
    upload_data(cities_data, "cities")
    upload_data(us_states_data, "us_states")
    upload_data(country_borders_data, "country_borders")
    upload_data(organizations_data, "organizations")

if __name__ == "__main__":
    main()