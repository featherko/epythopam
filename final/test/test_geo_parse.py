import asyncio
import unittest
from unittest.mock import MagicMock

import geopy.location
from final.fre.api_key import my_key
from final.fre.geo_parse import GeoParse
from final.fre.pony_db import Flat, db
from pony.orm import commit, db_session, delete

db.bind("sqlite", "test_geo_parse.db", create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def create_test_data():
    delete(p for p in Flat)
    commit()
    Flat(
        id=1,
        city="Москва",
        district="Москва",
        location="Москва",
        price=1,
        ppm=1,
        square=1,
    )
    commit()


create_test_data()


class TestGeocode(unittest.TestCase):
    long = 37.6172999
    lat = 55.755826

    def test_geo(self):
        create_test_data()
        point = geopy.point.Point(55.755826, 37.6172999)
        raw = {
            "address_components": [
                {
                    "long_name": "Moscow",
                    "short_name": "Moscow",
                    "types": ["locality", "political"],
                },
                {
                    "long_name": "Moscow",
                    "short_name": "Moscow",
                    "types": ["administrative_area_level_2", "political"],
                },
                {
                    "long_name": "Russia",
                    "short_name": "RU",
                    "types": ["country", "political"],
                },
            ],
            "formatted_address": "Moscow, Russia",
            "geometry": {
                "bounds": {
                    "northeast": {"lat": 56.0214609, "lng": 37.9678221},
                    "southwest": {"lat": 55.142591, "lng": 36.8032249},
                },
                "location": {"lat": 55.755826, "lng": 37.6172999},
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {"lat": 56.0214609, "lng": 37.9678221},
                    "southwest": {"lat": 55.142591, "lng": 36.8032249},
                },
            },
            "place_id": "ChIJybDUc_xKtUYRTM9XV8zWRD0",
            "types": ["locality", "political"],
        }
        address = "Moscow, Russia"
        location = geopy.location.Location(address, point, raw)
        mock = GeoParse(api_key=my_key())
        mock.geocode = MagicMock(return_value=location)
        actual_res = mock.geocode()
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(GeoParse(api_key=my_key()).parse())
        assert self.long == actual_res.longitude
        assert self.lat == actual_res.latitude
        with db_session:
            flat = Flat[1]
            assert self.long == flat.geo_long
            assert self.lat == flat.geo_lat
