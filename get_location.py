import pandas as pd
from geopy.geocoders import Nominatim

# Initialize a geocoder (Nominatim in this case)
geolocator = Nominatim(user_agent="geocoder")

# Read the CSV file
df = pd.read_csv('03.csv', sep=';')

# Create new columns for Latitude and Longitude
df['Latitude'] = None
df['Longitude'] = None

# Function to get latitude and longitude based on Location and Country
def get_lat_lon(location, country):
    location_info = geolocator.geocode(f"{location}, {country}")
    if location_info:
        return location_info.latitude, location_info.longitude
    else:
        return None, None

# Iterate through the rows and add latitude and longitude
for index, row in df.iterrows():
    location = row['Location']
    country = row['Country']
    lat, lon = get_lat_lon(location, country)
    df.at[index, 'Latitude'] = lat
    df.at[index, 'Longitude'] = lon

# Save the updated DataFrame back to the CSV file
df.to_csv('03.csv', sep=';', index=False)
