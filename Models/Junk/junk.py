import csv
import requests
import time  # For rate limiting

# Function to fetch lat/lon using Google Maps Geocoding API
def get_lat_lon(location):
    api_key = ""
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": location,
        "key": api_key
    }
    try:
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                lat = data['results'][0]['geometry']['location']['lat']
                lon = data['results'][0]['geometry']['location']['lng']
                return lat, lon
            else:
                print(f"Geocoding API request failed for {location}: {data['status']}")
        else:
            print(f"Geocoding API request failed for {location}: Status Code {response.status_code}")
    except Exception as e:
        print(f"Error fetching lat/lon for {location}: {str(e)}")
    return None, None

# Open the CSV file
input_file = "C:\\Users\\aloky\\OneDrive\\Desktop\\Marine_Classification\\Models\\Junk\\new.csv"
output_file = "newl.csv"

with open(input_file, "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    locations = list(reader)

# Add columns for lat/lon
fieldnames = reader.fieldnames + ["Latitude", "Longitude"]

# Open the output CSV file for writing
with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for location in locations:
        location_name = location["Location"]
        lat, lon = get_lat_lon(location_name)
        if lat is not None and lon is not None:
            location["Latitude"] = lat
            location["Longitude"] = lon
            writer.writerow(location)
        else:
            print(f"Failed to get lat/lon for {location_name}")

        # Add a small delay to avoid hitting rate limits
        time.sleep(0.1)  # Adjust as per API rate limits (10 requests per second recommended)

print(f"Location data with lat/lon saved to {output_file}")

