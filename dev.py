import os

# Set environment variables for this run
os.environ['CONNECTOR_NAME'] = 'geo-datasets'
os.environ['RUN_ID'] = 'local-dev'
os.environ['ENABLE_HTTP_CACHE'] = 'true'
os.environ['STORAGE_BACKEND'] = 'local'
os.environ['DATA_DIR'] = 'data'

# Run just the us_states asset to test the fix
from utils import validate_environment, upload_data
from assets.us_states.us_states import process_us_states

validate_environment()
us_states_data = process_us_states()
print(f"Schema: {us_states_data.schema}")
print(f"Number of rows: {len(us_states_data)}")
upload_data(us_states_data, "us_states")
print("Successfully uploaded us_states data")