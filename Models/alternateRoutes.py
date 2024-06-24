import numpy as np
import pandas as pd
from math import radians, sin, cos, sqrt, atan2
import folium
import Constants
import os

data_path = Constants.data_path
try:
    data = pd.read_csv(data_path, encoding='latin1')
except UnicodeDecodeError as e:
    print(f"Error decoding file: {e}")

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  
    return distance

def find_nearest_places(reference_place, places, fish_species):
    reference_lat, reference_lon = reference_place['Latitude'], reference_place['Longitude']
    places_with_distances = []
    visited_locations = set()
    fish_species = fish_species.lower()
    for place in places:
        if fish_species in place['Common Fish Species'].lower():
            distance = haversine(reference_lat, reference_lon, place['Latitude'], place['Longitude'])
            location_name = place['Location']
            if location_name not in visited_locations:
                places_with_distances.append((location_name, distance, place['Latitude'], place['Longitude']))
                visited_locations.add(location_name)
    places_with_distances.sort(key=lambda x: x[1])
    return places_with_distances[2:8]


def alternateRoutes(user_location, user_fish_species):
    location_row = data[data['Location'] == user_location]
    if location_row.empty:
        return "Invalid Location"
    available_fish_species = [species.strip().lower() for species in location_row['Common Fish Species'].iloc[0].split(',')]
    if user_fish_species.lower() not in available_fish_species:
        return "Invalid Fish Request"
    reference_place = {'Location': user_location, 'Latitude': location_row['Latitude'].iloc[0], 'Longitude': location_row['Longitude'].iloc[0]}
    nearest_places = find_nearest_places(reference_place, data.to_dict(orient='records'), user_fish_species)
    map_path = create_map(nearest_places, user_location)
    return nearest_places, map_path


def create_map(nearest_places, user_location):
    if not nearest_places:
        return "No nearest places found."
    user_coords = (nearest_places[0][2], nearest_places[0][3])  
    m = folium.Map(location=user_coords, zoom_start=12)
    for place in nearest_places:
        folium.Marker(
            location=[place[2], place[3]],
            popup=f"{place[0]}, Distance: {place[1]:.2f} km",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)
    map_dir = 'static/maps'
    os.makedirs(map_dir, exist_ok=True)
    map_filename = f"{user_location}_map.html"
    map_path = os.path.join(map_dir, map_filename)
    m.save(map_path)
    return map_filename