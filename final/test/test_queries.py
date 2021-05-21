import unittest

from final.fre.heatmap import db_query_hm
from final.fre.histo import db_query_hg
from final.fre.pony_db import Flat, db
from pony.orm import commit, db_session, delete

db.bind("sqlite", "test_avg.db", create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def create_easy_data():
    delete(p for p in Flat)
    commit()
    for i in range(4):
        Flat(
            id=i,
            city="city",
            district="district",
            location="location",
            price=i,
            ppm=i,
            square=i ** 2,
            geo_lat=1,
            geo_long=1,
        )
        commit()


class TestEasyAvgQueries(unittest.TestCase):
    create_easy_data()

    @db_session
    def test_ppm(self):
        print(db_query_hm()[:][0])
        _, _, avg_ppm = db_query_hm()[:][0]
        assert avg_ppm == 1.5

    @db_session
    def test_square(self):
        print(db_query_hg("city")[:][0])
        _, avg_square = db_query_hg("city")[:][0]
        assert avg_square == 3.5
