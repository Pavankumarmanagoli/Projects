from google.cloud import storage
import os
import json
import requests
import schedule
import threading
import time

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/pavanmanagoli/Downloads/DATA ENG2/NextBike/de2-425323-4c13d574ad33.json'
from google.cloud import storage
from google.oauth2 import service_account

# Specify your service account key file directly
credentials = service_account.Credentials.from_service_account_file(
    '/Users/pavanmanagoli/Downloads/DATA ENG2/NextBike/de2-425323-4c13d574ad33.json')

storage_client = storage.Client(credentials=credentials)

# The rest of your code remains the same...

# # Instantiates a client
# storage_client = storage.Client()

# The name for the new bucket
bucket_name = "nextbike_bucket"

# URL of NextBike API
url = 'https://api.nextbike.net/maps/nextbike-live.json'

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}.".format(
        source_file_name,
        destination_blob_name))

def job():
    # Make a GET request to the NextBike API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Open a file for writing
        with open('data.json', 'w') as f:
            # Write the data to a file
            for country in data['countries']:
              for city in country['cities']:
                for station in city['places']:
                    json.dump({
                        'country': country.get('country'),
                        'city': city.get('name'), 
                        'geopunkt': station.get('position'),
                        'place_type': station.get('type'),
                        'lat': station.get('lat'),
                        'bikes': station.get('bikes'),
                        'uid': station.get('uid'),
                        'bike_types': station.get('bike_types'),
                        'booked_bikes': station.get('booked_bikes'),
                        'bikes_available_to_rent': station.get('bikes_available_to_rent'),
                        'terminal_type': station.get('terminal_type'),
                        'name': station.get('name'),
                        'free_racks': station.get('free_racks'),
                        'bike_numbers': station.get('bike_numbers'),
                        'bike': station.get('bike'),
                        'lng': station.get('lng'),
                        'spot': station.get('spot'),
                        'bike_racks': station.get('bike_racks'),
                        'number': station.get('number'),
                    }, f)
                    f.write('\n')

        # Upload the file to GCS
        upload_blob(bucket_name, 'data.json', 'data.json')
    else:
        print(f'Request failed with status code {response.status_code}')

# Create a global flag for the running state of the loop
running = True

# Define stop function to listen to user input
def stop():
    global running
    while running:
        stop_input = input()
        if stop_input.lower() == 's':
            print('Stopping gracefully...')
            running = False

# Start stop function in a separate thread
stop_thread = threading.Thread(target=stop)
stop_thread.start()

# Schedule the job to be run every minute
schedule.every(1).minutes.do(job)

while running:
    # Run pending jobs
    schedule.run_pending()
    time.sleep(1)
