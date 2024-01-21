import os
import googlemaps
from typing import Optional


class GoogleMapsInfo:

    def __init__(self, lat, lon, place_id):
        self.lat = lat
        self.lon = lon
        self.place_id = place_id


class GoogleMapsManager:

    def __init__(self):
        # Would use some sort of secret manager instead
        api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        self.gmaps = googlemaps.Client(key=api_key)

    def get_google_maps_info(self, address, city, province_or_state) -> Optional[GoogleMapsInfo]:
        """Given an address, city, and province or state combination returns geo location info using Google Map API"""
        geocode_result = self.gmaps.geocode(f"{address}, {city}, ${province_or_state}")
        if geocode_result:
            if len(geocode_result) > 0:
                result = geocode_result[0]
                if 'geometry' in result and 'location' in result['geometry'] and 'place_id' in result:
                    lat = result['geometry']['location']['lat']
                    lon = result['geometry']['location']['lng']
                    place_id = result['place_id']
                    return GoogleMapsInfo(lat, lon, place_id)
        return None
