import os
import googlemaps
from typing import Optional


# Google is a bit stringent on what can be persisted. I think that place_id, latitude, and longitude are safe to persist
# I will double check
# https://stackoverflow.com/questions/20803805/terms-and-conditions-google-maps-can-i-store-lat-lng-and-address-components
class GoogleMapsInfo:

    def __init__(self, place_id):
        # https://developers.google.com/maps/documentation/places/web-service/place-id#save-id
        self.place_id = place_id


class GoogleMapsManager:

    def __init__(self):
        # Would use some sort of secret manager instead
        api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        self.gmaps = googlemaps.Client(key=api_key)

    def get_google_maps_info(self, address, city, province_or_state, lat, lon) -> Optional[GoogleMapsInfo]:
        """Given an address, city, and province or state combination returns geo location info using Google Map API"""
        geocode_result = self.gmaps.geocode(f"{address}, {city}, ${province_or_state}")
        if geocode_result:
            if len(geocode_result) > 0:
                result = geocode_result[0]
                if 'geometry' in result and 'location' in result['geometry'] and 'place_id' in result:
                    google_lat = result['geometry']['location']['lat']
                    google_lon = result['geometry']['location']['lng']
                    # Only using google for validation
                    if google_lat == lat and google_lon == lon:
                        place_id = result['place_id']
                        return GoogleMapsInfo(place_id)
        return None
