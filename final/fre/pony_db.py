"""Base for table with data."""
from pony.orm import *  # noqa: F403

db = Database()


class Flat(db.Entity):
    """Table of Flats."""

    id = PrimaryKey(int)  # noqa: A003
    city = Required(str)
    district = Required(str)
    location = Required(str)
    price = Required(int, size=64)
    ppm = Required(int)
    square = Required(float)
    geo_lat = Optional(float)
    geo_long = Optional(float)

    @property
    def address(self) -> str:
        """Return address in string."""
        return f"{self.city} {self.location}"

    def __repr__(self) -> str:  # noqa: D105
        return f"Flat {self.id} {self.address} {self.geo_lat} {self.geo_long}"


def db_bind() -> None:
    """Binding table to db."""
    db.bind("sqlite", "cian.db", create_db=True)
    db.generate_mapping(create_tables=True)
