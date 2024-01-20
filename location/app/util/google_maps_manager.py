import os
import googlemaps
from typing import Optional


class GoogleMapsManager:

    def __init__(self):
        # Would use some sort of secret manager instead
        api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        self.gmaps = googlemaps.Client(key=api_key)

    def get_lat_lon(self, address, city, province_or_state) -> Optional[(int, int)]:
        geocode_result = self.gmaps.geocode(f"{address}, {city}, ${province_or_state}")
        if geocode_result:
            if len(geocode_result) > 0:
                result = geocode_result[0]
                if 'geometry' in result and 'location' in result['geometry']:
                    lat = result['geometry']['location']['lat']
                    lon = result['geometry']['location']['lon']
                    return lat, lon
        return None
