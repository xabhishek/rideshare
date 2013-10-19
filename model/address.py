__author__ = 'gjacoby'

import geojson

class Address:
    address_id = None
    street_name = None
    city = None
    state = None
    country = None
    zipcode = None
    latitude = None
    longitude = None

    def __init__(self):
        pass

    def __init__(self, dict):
        self.address_id = dict["addressid"]
        self.street_name = dict.get("streetname")
        self.city = dict.get("city")
        self.state = dict.get("state")
        self.country = dict.get("country")
        self.zipcode = dict.get("zipcode")
        gjson = dict.get("location_json")
        if gjson is not None:
            coord = geojson.loads(gjson) #, object_hook=geojson.GeoJSON)
            self.longitude = coord["coordinates"][0]
            self.latitude = coord["coordinates"][1]

