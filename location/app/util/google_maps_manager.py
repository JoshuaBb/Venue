import os
import googlemaps
from typing import Optional
from dataclasses import dataclass, asdict


# Google is a bit stringent on what can be persisted. I think that place_id, latitude, and longitude are safe to persist
# I will double check
# https://stackoverflow.com/questions/20803805/terms-and-conditions-google-maps-can-i-store-lat-lng-and-address-components

@dataclass
class GoogleMapsInfo:
    place_id: int 

    def __init__(self, place_id):
        # https://developers.google.com/maps/documentation/places/web-service/place-id#save-id
        self.place_id = place_id

    def dict(self) -> dict[str, any]:
        return asdict(self)


class GoogleMapsManager:

    def __init__(self):
        # Would use some sort of secret manager instead
        api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        self.gmaps = googlemaps.Client(key=api_key)

    async def get_google_maps_info(self, address, city, province_or_state, lat, lon) -> Optional[GoogleMapsInfo]:
        """Given an address, city, and province or state combination returns geo location info using Google Map API"""
        geocode_result = self.gmaps.geocode(f"{address}, {city}, ${province_or_state}")
        if geocode_result:
            if len(geocode_result) > 0:
                result = geocode_result[0]
                if 'geometry' in result and 'location' in result['geometry'] and 'place_id' in result:
                    google_lat = round(result['geometry']['location']['lat'],3)
                    google_lon = round(result['geometry']['location']['lng'],3)
                    # Only using google for validation
                    if google_lat == round(lat,3) and google_lon == round(lon,3):
                        place_id = result['place_id']
                        return GoogleMapsInfo(place_id)
        return None
